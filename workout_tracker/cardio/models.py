from django.db import models
from core.models import Workout

# Create your models here.
class Cardio(models.Model):
      workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
      duration = models.DurationField()
      distance = models.FloatField(null=True, blank=True)  # Distance in kilometers or miles, depending on your preference
      EXERCISE_CHOICES = [
            ('run', 'Run'),
            ('cycle', 'Cycle'),
      ]
      exercise_type = models.CharField(max_length=10, choices=EXERCISE_CHOICES)