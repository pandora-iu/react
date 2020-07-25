from rest_framework import serializers

from ..models.Category import Category
from ..models.SourceType import SourceType
from django.conf import settings


class CategoryDetailSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created_at',
            'number_of_products',
            'icon_source',
            'icon_url'
        ]
        
    def get_icon_url(self, obj):
        if obj.icon_source == SourceType.URL:
            return obj.url
        elif obj.icon_source == SourceType.UPLOAD:
            return '{0}{1}'.format(settings.MEDIA_URL, obj.file)