from django.contrib import admin
from .models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',  'time_created',)
    list_display_links = ('id', 'title', )



