from rest_framework.generics import RetrieveAPIView

from ..models.Category import Category
from ..serializers.CategoryDetailSerializer import CategoryDetailSerializer


class CategoryDetailView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Category.objects.all()