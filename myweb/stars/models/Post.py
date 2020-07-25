from uuid import uuid4

from django.db import models
from django.utils import timezone

from .PostType import PostType
from .Product import Product
from .SourceType import SourceType
from ..utils import get_file_path


class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4)
    title = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, related_name='posts', on_delete=models.CASCADE)
    post_type = models.CharField(choices=PostType.choices(), max_length=10)
    source_type = models.CharField(choices=SourceType.choices(), max_length=10)
    file = models.FileField(upload_to=get_file_path, blank=True, null=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ['-updated_at']