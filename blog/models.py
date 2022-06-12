from django.db import models

from user.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    class Meta:
        db_table = "article"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(to="Category", verbose_name="카테고리")
    content = models.TextField(blank=True, null=True)
    # img = models.FileField(upload_to='uploads/%Y%m%d', blank=True, null=True)
    # like_cnt = models.IntegerField(default=0)
    # article_hits = models.IntegerField(default=0)

    def __str__(self):
        return self.title