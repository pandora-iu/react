from rest_framework.generics import RetrieveUpdateAPIView

from ..models.Product import Product
from ..serializers.ProductSerializer import ProductSerializer


class ProductDetailView(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    lookup_field = 'id'

    queryset = Product.objects.all()