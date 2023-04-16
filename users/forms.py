from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class BootstrapAuthenticationForm(forms.Form):
    """Authentication form which uses boostrap CSS."""
    email = forms.EmailField(label=("Email"),
                               widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder':'Email'}))
    password = forms.CharField(label=("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

    class Meta:
        fields = ('emai', 'password')

