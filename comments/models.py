from django.db import models
from django.contrib.auth import get_user_model
from blogapp.models import Article


class CommentModel(models.Model):
    MARKS = ((2, 2),
            (3, 3),
           (4, 4),
          (5, 5))

    content = models.TextField(max_length=300)
    user = models.ForeignKey(get_user_model(), db_index=True, on_delete=models.PROTECT)
    mark = models.IntegerField(choices=MARKS)
    article = models.ForeignKey(Article, on_delete=models.PROTECT, db_index=True, null=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ['-id']

