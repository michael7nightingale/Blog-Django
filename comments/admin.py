from django.contrib import admin
from .models import *


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'user', 'mark']
    list_display_links = ['id', ]
