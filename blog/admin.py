from django.contrib import admin

from .models import Article as ArticleModel
from .models import Category as CategoryModel
from .models import Comment as CommentModel


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
# Register your models here.
admin.site.register(ArticleModel)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(CommentModel)