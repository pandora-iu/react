from rest_framework.generics import ListAPIView

from ..models.Product import Product
from ..pagination.DetailListPagination import DetailListPagination
from ..serializers.PostSerializer import PostSerializer



class PostView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = DetailListPagination
    lookup_field = 'id'

    def get_queryset(self):
        product = Product.objects.filter(id=self.kwargs.get(self.lookup_field)).first()
        return product.posts.all()