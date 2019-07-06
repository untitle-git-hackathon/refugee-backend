from django.db import models
from .location import Location

class Refugee(models.Model):
    objects = models.Manager()
    
    name = models.CharField(max_length=10)
    location_id = models.OneToOneField(to=Location, on_delete=models.CASCADE)
