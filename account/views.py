from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.views import APIView
from  . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerialization , UserDetailSerializer ,UserProfileSerializer

# Create your views here.



    
    # Registration Part 
     
class userRegistration(APIView):       
    serializer_class = RegistrationSerialization
       
    def post(self, request):
        serializer = self.serializer_class(data=request.data)          
        if serializer.is_valid():
            user =  serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid" , uid)
            confirm_link = f"https://car-repair-backend-drf.vercel.app/account/active/{uid}/{token}"
            email_subject = "Confirm Your Email Now"
            email_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link})
            email = EmailMultiAlternatives(email_subject , "" , to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            
            return Response("Check Your E-mail Confirmation..")
            
        return Response (serializer.errors)
 
 
 
               
def activate(request, uid64, token): 
    print(uid64)
    print(token)
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activated! You can now log in.")
    
        return redirect('https://foysal777.github.io/car-reapir-fronted/login.html')
        
    else:
        messages.error(request, "Activation link is invalid or has expired. Please register again.")
        return redirect('register')





# for login 

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request , email=email, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)
    


 
    
class UserDetailApiView(APIView):
    def get(self, request):
        user = request.user  
        serializer = UserDetailSerializer(user)  
        print(serializer.data)
        return Response(serializer.data)
    
 

    def post(self, request, *args, **kwargs):
        serializer = UserDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserLogoutView(APIView):
    def get(self, request):
        user = request.user
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()

        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    

class adminAcess(APIView):
    def get(self, request):
        user = request.user
        print(user)
        print(user.is_staff)
        if user.is_authenticated:
           
            return Response({"is_admin": user.is_staff})
        return Response({"is_admin": False})
    
    
    

class EditProfileView(APIView):
    # permission_classes = [IsAuthenticated]

    def put(self, request):
        # Get the current authenticated user
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)