# urls.py
from django.urls import path
from .views import product_list,FeedbackAPIView

urlpatterns = [
    path('partsadd/', product_list, name='product-list'),
    path('feedback/', FeedbackAPIView.as_view(), name='feedback')
]
