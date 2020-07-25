from uuid import uuid4

from django.db import models
from django.utils import timezone

from .Category import Category


class Product(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4)
    title = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=1000, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    cost = models.FloatField(blank=False, null=False, default=100)
    categories = models.ManyToManyField(Category, related_name='products')

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    @property
    def number_of_posts(self):
        return self.posts.count()

    @property
    def number_of_categories(self):
        return self.categories.count()