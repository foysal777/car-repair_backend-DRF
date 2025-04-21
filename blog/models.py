from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    posted_by = models.CharField(max_length=100)
    date_posted = models.DateField()
    main_image = models.CharField(max_length=244, default='')

    def __str__(self):
        return self.title

 

class Appointment(models.Model):
    post = models.ForeignKey(User, related_name='post', on_delete=models.CASCADE)
    appointment_date = models.DateField()
    client_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Appointment with {self.client_name} on {self.appointment_date}"


class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank= True , null=True)
    