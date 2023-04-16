"""
Definition of models.
"""

from django.db import models


class Awards(models.Model):
    image = models.ImageField(upload_to='awards', verbose_name='Достижения')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

