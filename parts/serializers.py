# serializers.py
from rest_framework import serializers
from .models import Parts, Feedback , Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = ['id', 'title', 'price', 'image_url']
        
        
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'name', 'rating', 'comment', 'created_at']
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'