from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Appointment
from .serializers import AppointmentSerializer

@api_view(['GET', 'POST'])
def CreateAppointment(request):
    if request.method == 'GET':
        
        appointments = Appointment.objects.all()
        total_appointments = appointments.count()
        serializer = AppointmentSerializer(appointments, many=True)
        
        
        return Response({
            'total_appointments': total_appointments,
            'appointments': serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
       
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def get_appointment_by_id(request, id):
    try:
        appointment = Appointment.objects.get(id=id)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Appointment.DoesNotExist:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)