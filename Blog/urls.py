from datetime import datetime

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', include('app.urls')),
    path('users/', include('users.urls')),
    path('blog/', include('blogapp.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)