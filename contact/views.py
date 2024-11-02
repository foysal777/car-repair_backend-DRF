# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactSerializer
from django.conf import settings

class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            # Extract the validated data
            data = serializer.validated_data
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            phone_number = data.get('phone_number')
            comments = data.get('comments')
            
            # Compose the email content
            subject = f"New Message from {first_name} {last_name}"
            message = f"Name: {first_name} {last_name}\nEmail: {email}\nPhone: {phone_number}\n\nMessage:\n{comments}"
            recipient = [settings.EMAIL_HOST_USER]

            # Send the email
            send_mail(subject, message, email, recipient, fail_silently=False)

            return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
