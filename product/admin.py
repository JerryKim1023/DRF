from django.contrib import admin
from product.models import Event as EventModel
from product.models import Product as ProductModel
from product.models import Review as ReviewModel

from django.utils.safestring import mark_safe

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        # "thumbnail",
        "desc",
        "created_at",
        "show_expired_date",
        "is_active",
        "thumbnail_preview",
    )
    def thumbnail_preview(self, obj):
        return mark_safe(f'<img src="/product/thumbnail/{obj.id}/" height="100px"/>')
        # 여기서 이미지 크기 조절도 가능

    thumbnail_preview.short_decription = "Thumbnail"

admin.site.register(EventModel, EventAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        # "thumbnail",
        "desc",
        "created_at",
        "show_expired_date",
        "is_active",
        "thumbnail_preview",
    )
    def thumbnail_preview(self, obj):
        return mark_safe(f'<img src="/product/thumbnail/{obj.id}/" height="100px"/>')
        # 여기서 이미지 크기 조절도 가능

    thumbnail_preview.short_decription = "Thumbnail"

admin.site.register(ProductModel, ProductAdmin)

admin.site.register(ReviewModel)