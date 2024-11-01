# urls.py
from django.urls import path
from .views import CreateAppointment,get_appointment_by_id

urlpatterns = [
    path('appoint_details/', CreateAppointment, name='create_appointment'),
    path('appointments/<int:id>/', get_appointment_by_id, name='appointment-detail'), 

]
