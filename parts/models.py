# models.py
from django.db import models

class Parts(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title
