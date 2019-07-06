from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.TextField()
