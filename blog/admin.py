from django.contrib import admin

from .models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
# Register your models here.
admin.site.register(Article)
admin.site.register(Category, CategoryAdmin)