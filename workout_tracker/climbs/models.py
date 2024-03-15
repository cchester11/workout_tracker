from django.db import models
from core.models import Workout

# Create your models here.
class Climbing(models.Model):
      workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

class KilterBoarding(models.Model):
      climbing = models.ForeignKey(Climbing, on_delete=models.CASCADE)
      climbs_done = models.PositiveIntegerField()

class FreeClimb(models.Model):
      climbing = models.ForeignKey(Climbing, on_delete=models.CASCADE)
      completed = models.BooleanField()
      difficulty = models.CharField(max_length=10)  # e.g., 'V1', 'V2', etc.