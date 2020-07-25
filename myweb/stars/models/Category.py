from uuid import uuid4

from django.db import models
from django.utils import timezone
from .SourceType import SourceType
#from ..utils import get_file_path


class Category(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4)
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    icon_source = models.CharField(choices=SourceType.choices(), max_length=10, default="URL")
    file = models.ImageField(blank=True, null=True)
    url = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    @property
    def number_of_products(self):
        return self.products.count()