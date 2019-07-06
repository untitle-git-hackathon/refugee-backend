from django.db import models
from .story import Story

class Qa(models.Model):
    correct_answer_image = models.CharField(max_length=30)
    wrong_answer_image = models.CharField(max_length=30)
    story = models.OneToOneField(to=Story, on_delete=models.CASCADE)
