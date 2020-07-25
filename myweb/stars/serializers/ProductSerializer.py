from rest_framework import serializers

from ..models.Product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        depth = 1
        fields = [
            'id',
            'title',
            'created_at',
            'description',
            'updated_at',
            'cost',
            'number_of_categories',
            'categories',
            'number_of_posts',
            'posts',
        ]
