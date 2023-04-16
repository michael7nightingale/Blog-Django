from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from blogapp.forms import ArticleForm, ArticleDeleteForm
from .models import *
from app.views import DataMixin
from comments.forms import CommentForm
from comments.models import CommentModel



# ___________________________Common_views_for_users_____________________________________#


class ArticlesView(ListView, DataMixin):
    template_name = 'blogapp/articles.html'
    context_object_name = "articles"
    model = Article
        
    def get_queryset(self):
        return Article.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Статьи"
        context['title'] = "Publicated arciles"
        c_def = self.get_context_user()
        return dict(list(context.items()) + list(c_def.items()))


class ArticleSingleView(FormMixin, DetailView, DataMixin):
    template_name = "blogapp/article.html"
    context_object_name = 'article'
    model = Article
    slug_url_kwarg = 'a_slug'
    form_class = CommentForm
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentModel.objects.filter(article__slug=self.object.slug)
        return context

    def get_success_url(self):
        return reverse('blog_article', kwargs={"a_slug": self.object.slug})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form=form)
        else:
           return self.form_invalid(form=form)

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            CommentModel.objects.create(content=form.cleaned_data['content'], 
                                        article=self.object, 
                                        user=self.request.user, 
                                        mark=form.cleaned_data['mark']).save()
        else:
            return redirect("login")
        return super(ArticleSingleView, self).form_valid(form)


# ___________________________Views_for_administration__________________________________#


class BlogView(PermissionRequiredMixin, TemplateView, DataMixin):
    permission_required = ("superuser", 'stuff')
    # permission_denied_message = "Доступ запрещен"
    template_name = "blogapp/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Блог"
        c_def = self.get_context_user()
        return dict(list(context.items()) + list(c_def.items()))


class AddArticleView(PermissionRequiredMixin, CreateView):
    """Добавление новой статьи"""
    permission_required = ("superuser", 'stuff')
    form_class = ArticleForm
    template_name = 'blogapp/add_article.html'



    def form_valid(self, form):
        form.save()
        return redirect('blog_articles')


def createArticle(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm()
    return render(request, 'blogapp/add_article.html', {'form': form})


class UnpublishedArticlesView(PermissionRequiredMixin, ListView, DataMixin):
    """Список неопубликованных статей"""
    permission_required = ("superuser", 'stuff')
    model = Article
    context_object_name = 'articles'
    template_name = "blogapp/unpublished_articles.html"

    def get_queryset(self):
        return self.model.objects.filter(is_published=False)

    def get_context_data(self, **kwargs):
        context: dict = super().get_context_data(**kwargs)
        context['title'] = "Неопубликованные статьи"
        return dict(
            list(context.items()) + list(self.get_context_user().items())
        )


@permission_required(perm=('superuser', 'stuff'), login_url="login", raise_exception=False)
def edit_article(request, a_slug):
    """Изменение существующей статьи"""
    dm = DataMixin()
    object_ = Article.objects.get(slug=a_slug)

    if request.method == 'GET':
        form = ArticleForm(instance=object_)
        formDelete = ArticleDeleteForm()

    elif request.method == 'POST':
        formDelete = ArticleDeleteForm()
        if 'commit_delete' in request.POST:
            if request.POST['commit_delete'] == object_.title[::-1]:
                object_.delete()
                return redirect("blog_unpublished_articles")

        form = ArticleForm(request.POST, instance=object_)
        if form.is_valid():
            form.save()
            return redirect("blog_article_edit", a_slug)

    context = dm.get_context_user()
    context['title'] = 'Редактор статьи'
    context['article'] = object_
    context['form'] = form
    context['reversed_title'] = object_.title[::-1]
    context['form_delete'] = formDelete

    return render(request, "blogapp/edit_aricle.html", context)


def delete_article(request, a_pk):
    return render(request, 'blogapp/blog.html')


