# admission/models.py

from django.db import models

class Student(models.Model):
    course_applied = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    religion = models.CharField(max_length=50)
    present_address = models.TextField()
    permanent_address = models.TextField()
    nationality = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name
