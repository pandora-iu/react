from rest_framework import serializers

from ..models.Post import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'product',
            'post_type',
            'source_type',
        ]