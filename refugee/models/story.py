from django.db import models
from .refugee import Refugee

class Story(models.Model):
    objects = models.Manager()

    message = models.TextField()
    refugee = models.OneToOneField(to=Refugee, on_delete=models.CASCADE)
    is_from_refugee = models.BooleanField()
    image_url = models.TextField(blank=True)
