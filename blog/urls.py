from django.urls import path
from .views import PostListCreateAPIView ,TotalPostCountAPIView , delete_post, GalleryView

urlpatterns = [
    path('total-blog-count/', TotalPostCountAPIView.as_view(), name='total-blog'),
    path('post/', PostListCreateAPIView.as_view(), name='blog'),
    path('post/delete/<int:post_id>/', delete_post, name='delete_post'),
    path('gallery/', GalleryView.as_view(), name='Galleryimages'),

  
]
