# urls.py
from django.urls import path
from .views import product_list

urlpatterns = [
    path('partsadd/', product_list, name='product-list'),
]
