# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Parts, Feedback, Order
from rest_framework.views import APIView
from .serializers import ProductSerializer, FeedbackSerializer
import uuid
from django.shortcuts import render


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Parts.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackAPIView(APIView):
    def get(self, request, *args, **kwargs):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(
            feedbacks, many=True)  # Serialize the data
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateMockOrder(APIView):
    def post(self, request):
        title = request.data.get("title")
        price = request.data.get("price")

        order = Order.objects.create(
            title=title,
            price=price,
            transaction_id=str(uuid.uuid4())
        )

        # Return fake payment URL
        fake_payment_url = f"http://localhost:8000/mock-payment/{order.transaction_id}/"
        return Response({"payment_url": fake_payment_url})


def mock_payment_page(request, transaction_id):
    return render(request, "mock_payment.html", {"transaction_id": transaction_id})


def mock_payment_success(request, transaction_id):
    order = Order.objects.get(transaction_id=transaction_id)
    order.paid = True
    order.save()
    return render(request, "payment_result.html", {"result": "success"})


def mock_payment_fail(request, transaction_id):
    return render(request, "payment_result.html", {"result": "fail"})


def mock_payment_cancel(request, transaction_id):
    return render(request, "payment_result.html", {"result": "cancel"})
