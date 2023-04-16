from django import forms
from .models import CommentModel


class CommentForm(forms.Form):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
                             attrs={"class": "form-control", 
                             "placeholder": "Комментарий: "}))
    mark = forms.CharField(
        label='Оценка',
        widget=forms.Select(
              attrs={"class": "form-control",
              "placeholder": "Оценка записи"}, choices=CommentModel.MARKS))


    class Meta:
        # model = CommentModel
        fields = ("content", 'mark')

