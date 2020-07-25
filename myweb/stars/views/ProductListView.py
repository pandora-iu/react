from rest_framework.generics import ListAPIView

from ..models.Product import Product
from ..pagination.DetailListPagination import DetailListPagination
from ..serializers.ProductSerializer import ProductSerializer


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = DetailListPagination
    queryset = Product.objects.all()