from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from .forms import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('statistics/', include(
        [path('last-users/', LastUsersView.as_view(), name='users_last_users'),
         path('last-comments/', LastCommentsView.as_view(), name='users_last_comments'), ]
    )),

    
]