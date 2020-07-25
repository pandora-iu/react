from django.conf.urls import url

from .views.CategoryDetailView import CategoryDetailView
from .views.CategoryListView import CategoryListView
"""from .views.ModelDetailView import ModelDetailView
from .views.ModelListView import ModelListView"""
from .views.PostView import PostView
from .views.ProductDetailView import ProductDetailView
from .views.ProductListView import ProductListView

urlpatterns = [
    url(r'categories/list', CategoryListView.as_view(), name='categories-list'),
    url(r'categories/(?P<id>[0-9a-f-]+)/$', CategoryDetailView.as_view(), name='categories-detail'),
    url(r'products/(?P<id>[0-9a-f-]+)/posts/$', PostView.as_view(), name='products-posts-list'),
    url(r'products/list', ProductListView.as_view(), name='products-list'),
    url(r'products/(?P<id>[0-9a-f-]+)/$', ProductDetailView.as_view(), name='products-detail'),

]