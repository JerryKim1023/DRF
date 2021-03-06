from django.db import models

from user.models import User as UserModel

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

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(to="Category", verbose_name="카테고리")
    content = models.TextField(blank=True, null=True)
    # img = models.FileField(upload_to='uploads/%Y%m%d', blank=True, null=True)
    # like_cnt = models.IntegerField(default=0)
    # article_hits = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    class Meta:
        db_table = "comment"

    def __str__(self):
        return f"{self.user} : {self.content}"

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()