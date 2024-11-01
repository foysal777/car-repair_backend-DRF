
from django.urls import path
from .views import userRegistration, UserLoginApiView, activate ,adminAcess, UserDetailApiView,UserLogoutView

urlpatterns = [
    path('register/' , userRegistration.as_view() , name= 'register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('active/<uid64>/<token>/', activate, name = 'activate'),
    path('user/details/', UserDetailApiView.as_view(), name='user-details'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('adminAcess/', adminAcess.as_view(), name='user-profile'),
]