from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Gallery
from .serializers import PostSerializer, GallerySerializer
from rest_framework.decorators import api_view


class PostListCreateAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)




class TotalPostCountAPIView(APIView):
    def get(self, request):
        total_posts = Post.objects.count() 
        data = {
            'total_posts': total_posts
        }
        return Response(data)
    
class GalleryView(api_view):
    def get(self, request):
        gallery = Gallery.objects.all()
        serializers = GallerySerializer(gallery, many = True)
        return Response(serializers.data)
    
    def post(self, request):
        serializers = GallerySerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)