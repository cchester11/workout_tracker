from django.db import models
from core.models import Workout

# Create your models here.
class Weights(models.Model):
      workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
      name = models.CharField(max_length=100)
      sets = models.PositiveIntegerField()
      intervals_per_set = models.PositiveIntegerField()