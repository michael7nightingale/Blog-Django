from django.contrib import admin
from .models import User


@admin.register(User)
class UserAmin(admin.ModelAdmin):
    list_display = ('id', 'username', "password", "email")

