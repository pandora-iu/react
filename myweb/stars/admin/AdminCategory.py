from django.contrib import admin
from django.utils.html import format_html
from ..models.Category import Category
from ..models.SourceType import SourceType
from django.conf import settings


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = [
        'icon_url',
        'title',
        'created_at',
        'number_of_products'
    ]
    

    def icon_url(self, obj):
        if obj.icon_source == SourceType.URL:
            return format_html(
                '<img src="{0}" height=30 width=30 />',
                obj.url
            )
        elif obj.icon_source == SourceType.UPLOAD:
            return format_html(
                '<img src="{0}{1}" height=30 width=30 />',
                settings.MEDIA_URL,
                obj.file
            )
    icon_url.short_description = "Icon"