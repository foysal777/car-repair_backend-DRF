# serializers.py
from rest_framework import serializers
from .models import Parts

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parts
        fields = ['id', 'title', 'price', 'image_url']
