
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date = models.DateField()
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_number = models.CharField(max_length=20)
    services = models.JSONField()  

    def __str__(self):
        return f"Appointment for {self.name} on {self.date}"
