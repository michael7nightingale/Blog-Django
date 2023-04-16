from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    BOOL_CHOICES = (
        (True, "К публикации"),
        (False, "Отложенная публикация")
    )

    title = forms.CharField(label='Заголовок статьи',
                            widget=forms.TextInput(
                            {'class': 'form-control',
                             'placeholder': 'заголовок'}))
    content = forms.CharField(label='Содержание статьи',
                            widget=forms.Textarea(
                            {'class': 'form-control',
                             'placeholder': 'содержание'}))
    image = forms.ImageField(label='Image', required=False,
                            widget=forms.FileInput(
                            {'class': 'form-control',
                             'placeholder': 'image'}))
    is_published = forms.BooleanField(required=False, label='Статус',
                            widget=forms.Select(
                            attrs ={'class': 'form-control'}, choices=BOOL_CHOICES))
    slug = forms.SlugField(label='Слаг статьи',
                           widget=forms.TextInput(
                               {'class': "form-control",
                                'placeholder': 'слаг'}))

    class Meta:
        model = Article
        fields = ('title', 'content', 'image', 'is_published', 'slug')
        # REQUIRED_FIELDS = ('title', 'content', 'image',  'is_published', 'slug')


class ArticleDeleteForm(forms.Form):
    commit_delete = forms.CharField(label='Введите текст, чтобы продолжить',
                                    widget=forms.TextInput(
                                        attrs={"class": 'form-control',
                                               "placeholder": "текст"}
                                    ))

    class Meta:
        fields = ('commit_delete', )

