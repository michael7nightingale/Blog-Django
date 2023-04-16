"""
Definition of forms.
"""

from django import forms
from .models import Awards


class AddAwardForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок достижения',
                            widget=forms.TextInput(
                            {'class': 'form-control',
                             'placeholder': 'заголовок'}))
    content = forms.CharField(label='Содержание достижения',
                            widget=forms.Textarea(
                            {'class': 'form-control',
                             'placeholder': 'содержание'}))
    image = forms.ImageField(label='Изображение', required=False,
                            widget=forms.FileInput(
                            {'class': 'form-control',
                             'placeholder': 'image'}))

    class Meta:
        model = Awards
        fields = ('title', 'content', 'image')


