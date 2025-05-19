from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Gallery , Project
from .serializers import PostSerializer, GallerySerializer , ProjectSerializers
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
    
class GalleryView(APIView):
    def get(self,request ,format = None):
        category = request.query_params.get('category',None)
       
        if category:
           images = Gallery.objects.filter(category=category)
        
        else:
           images = Gallery.objects.all()
        serializers = GallerySerializer(images, many = True , context = {'request' : request})
        return Response(serializers.data)
    
    def post(self, request , format =None ):
        serializers = GallerySerializer(data = request.data , context= {'request' : request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors , status=status.HTTP_400_BAD_REQUEST)
    
class ProjectAPIView(APIView):

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializers(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    