from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page

from .views import *


urlpatterns = [
    path("", cache_page(120)(BlogView.as_view()), name='blog_'),
    path('add_article/', createArticle, name='blog_add_article'),
    path('articles/', include([
        path('', cache_page(20)(ArticlesView.as_view()), name='blog_articles'),
        path('published/', cache_page(20)(ArticlesView.as_view()), name='blog_articles'),
        path("unpublished/", cache_page(20)(UnpublishedArticlesView.as_view()), name="blog_unpublished_articles"),
        path('<slug:a_slug>/', ArticleSingleView.as_view(), name='blog_article'),
        path("publish/<slug:a_slug>/", edit_article, name='blog_article_edit'),
        path("delete/<int:a_pk>/", delete_article, name='blog_article_delete'),
                ])
         ),
    path('articles/<slug:a_slug>', ArticleSingleView.as_view(), name='blog_article'),

]

from django.views.static import serve as mediaserve


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += [
        re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.MEDIA_ROOT}),
        re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]
