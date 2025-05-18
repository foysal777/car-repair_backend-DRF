from rest_framework import serializers
from .models import Post, Appointment, Gallery , Project

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'posted_by', 'date_posted', 'main_image']  


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
        
class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all_'
        