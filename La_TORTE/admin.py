from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image_detail.url} width="100" height="110"')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'url', 'popular', 'draft', 'category')
    list_editable = ('draft', 'popular', 'category')
    readonly_fields = ("get_image",)
    inlines = [ProductDetailInline,]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')


@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    """Изображения товара"""
    list_display = ("product", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image_detail.url} width="50" height="60"')



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("name", "url")
    list_display_links = ("name",)