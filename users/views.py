from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import *
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, login
from passlib.hash import django_pbkdf2_sha256

from .forms import *
from comments.models import CommentModel


User = get_user_model()


def login_view(request):
    form = BootstrapAuthenticationForm
    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.get(email=email)
        if django_pbkdf2_sha256.verify(password, user.password):
            login(request, user)
            return redirect('home')
    context = {'form': form,
               'title': 'Вход в систему'}

    return render(request, 'users/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('home')


class RegisterView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        email = self.request.POST['email']
        user = User.objects.create(username=username,
                                   email=email,
                                   password=password)
        user.set_password(password)
        user.save()
        login(self.request, user)
        return redirect("home")
        

class LastUsersView(ListView):
    template_name = 'users/last_users.html'
    model = User
    context_object_name = 'users'

    def get_queryset(self):
        return self.model.objects.all()[:20]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Последние пользователи'
        return context


class LastCommentsView(ListView):
    template_name = 'users/last_comments.html'
    model = CommentModel
    context_object_name = 'comments'

    def get_queryset(self):
        return self.model.objects.all()[:20]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Последние комментарии'
        return context

