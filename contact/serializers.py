# serializers.py

from rest_framework import serializers

class ContactSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=15, allow_blank=True, required=False)
    comments = serializers.CharField()
