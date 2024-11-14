from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerialization(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'confirm_password']
       

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
       
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Match"})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error' : "Email Already Exists."})      
        
        account = User(username = username , first_name = first_name , last_name = last_name, email = email )
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
     


# for login 

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)     
    
    
    
    
# For user details 
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
  
  
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
    