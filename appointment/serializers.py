from .models import Appointment
from rest_framework import serializers


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [ 'id' ,'name', 'phone', 'email', 'date', 'car_brand', 'car_model', 'car_number', 'services']