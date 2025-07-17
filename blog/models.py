from django.db import models
from django.contrib.auth.models import User


CATEGORY_CHOICES = [
        ('Brakes', 'Brakes'),
        ('Suspension', 'Suspension'),
        ('Wheels', 'Wheels'),
        ('Steering', 'Steering'),
        ('Transmission', 'Transmission'),
    ]

class Post(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=100)
    date_posted = models.DateField()
    main_image = models.CharField(max_length=944, default='')

    def __str__(self):
        return self.title

 

class Appointment(models.Model):
    post = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    client_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Appointment with {self.client_name} on {self.appointment_date}"


class Gallery(models.Model):
    
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=40 , choices=CATEGORY_CHOICES)
    image = models.URLField(blank= True , null=True , max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    image = models.URLField(blank=True, null= True , max_length=1000)
        