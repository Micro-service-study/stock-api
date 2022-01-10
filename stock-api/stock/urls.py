from django.urls import path

from .views.stock import stock, stockDetails
from .views.product import products

urlpatterns = [
  path('stock', stock),
  path('products', products),
  path('stock/<str:id>', stockDetails),
]