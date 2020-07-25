from rest_framework import serializers

from ..models.Category import Category


class CategoryListSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'details',
        ]

    def get_details(self, obj):
        return "/api/{0}/{1}".format(obj._meta.verbose_name_plural, obj.id)
