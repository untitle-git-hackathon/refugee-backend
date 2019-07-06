from django.db import models
from .refugee import Refugee

class Story(models.Model):
    message = models.TextField()
    refugee_id = models.OneToOneField(to=Refugee, on_delete=models.CASCADE)
    is_from_refugee = models.BooleanField()
    image_url = models.TextField()
