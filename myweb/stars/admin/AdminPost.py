from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

from ..models.Post import Post
from ..models.SourceType import SourceType


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = [
        'title',
        'product_url',
        'created_at',
        'updated_at',
        'post_type',
        'source_type',
        'source_url'
    ]
    list_filter = [
        'post_type',
        'source_type'
    ]
    readonly_fields = [
        'created_at',
        'updated_at'
    ]

    def product_url(self, obj):
        return format_html(
            '<a href="/admin/products/product/{0}/change/" target="_blank">{1}</a>',
            obj.product.id,
            obj.product
        )

    product_url.short_description = "Product"

    def source_url(self, obj):
        if obj.source_type == SourceType.YOUTUBE:
            return format_html(
                '<a href="{0}" target="_blank">{0}</a>',
                obj.url
            )
        elif obj.source_type == SourceType.UPLOAD:
            return format_html(
                '<a href="{0}{1}" target="_blank">{1}</a>',
                settings.MEDIA_URL,
                obj.file
            )

    source_url.short_description = "URL"