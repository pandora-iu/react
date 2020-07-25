from django.contrib import admin

from ..models.Product import Product


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = [
        'title',
        'cost',
        'created_at',
        'updated_at',
        'number_of_posts',
        'get_categories',
        'number_of_categories'
    ]
    readonly_fields = [
        'created_at',
        'updated_at'
    ]
    list_filter = [
        'categories'
    ]

    def get_categories(self, obj):
        return [category.title for category in obj.categories.all()]

    get_categories.short_description = "Categories"