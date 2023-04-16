from django.urls import reverse
from django.db import models


def generate_slug(title: str):
    return str(title).lower().replace(' ', '-')


class Article(models.Model):

    class Publicate(models.Choices):
        TO_PUBLISH = True, "Опубликовать сейчас"
        NOT_TO_PUBLISH = False, "Опубликовать позже"

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='articles', blank=True, null=True)
    time_created = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    slug = models.SlugField(default=generate_slug(title))

    class Meta:
        abstract = False
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-time_created']

    def get_absolute_url(self):
        return '/blog/articles/' + str(self.slug)

