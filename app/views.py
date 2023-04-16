from datetime import datetime
from typing import Optional
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.views import *
from django.contrib.auth import logout, login

from .forms import *
from .models import Awards


class DataMixin:
    def get_context_user(self):
        context = {'year': datetime.now().year}
        return context


class Home(TemplateView, DataMixin):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return dict(
            tuple(context.items()) + tuple(self.get_context_user().items())
        )


class Contact(TemplateView, DataMixin):
    template_name = 'app/contact.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Связь"
        return dict(
            tuple(context.items()) + tuple(self.get_context_user().items())
        )


class About(TemplateView, DataMixin):
    template_name = 'app/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Обо мне"
        context['awards'] = Awards.objects.all()
        return dict(
            tuple(context.items()) + tuple(self.get_context_user().items())
        )


class AddAward(CreateView, DataMixin):
    model = Awards
    template_name = 'app/add_award.html'
    form_class = AddAwardForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавить достижение"
        return dict(
            tuple(context.items()) + tuple(self.get_context_user().items())
        )

    def form_valid(self, form):
        form.save()
        return redirect('about')