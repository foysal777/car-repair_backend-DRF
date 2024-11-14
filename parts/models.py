
from django.db import models

class Parts(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"