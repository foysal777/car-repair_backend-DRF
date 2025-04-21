from rest_framework import serializers
from .models import Post, Appointment, Gallery

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'posted_by', 'date_posted', 'main_image']  


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'