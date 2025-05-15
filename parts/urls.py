# urls.py
from django.urls import path
from .views import product_list,FeedbackAPIView
from .views import (
    CreateMockOrder,
    mock_payment_page,
    mock_payment_success,
    mock_payment_fail,
    mock_payment_cancel,
)

urlpatterns = [
    path('partsadd/', product_list, name='product-list'),
    path('feedback/', FeedbackAPIView.as_view(), name='feedback'),
    # payment 
    path('api/create-mock-order/', CreateMockOrder.as_view(), name='create-mock-order'),
    path('mock-payment/<str:transaction_id>/', mock_payment_page, name='mock-payment'),
    path('mock-payment/success/<str:transaction_id>/', mock_payment_success),
    path('mock-payment/fail/<str:transaction_id>/', mock_payment_fail),
    path('mock-payment/cancel/<str:transaction_id>/', mock_payment_cancel),
]
