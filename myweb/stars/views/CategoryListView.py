from rest_framework.generics import ListAPIView

from ..models.Category import Category
from ..serializers.CategoryListSerializer import CategoryListSerializer


class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()