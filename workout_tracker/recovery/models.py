from django.db import models
from core.models import Workout


# Create your models here.
class Recover(models.Model):
      workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
      DURATION_CHOICES = [
            ("15", "15 minutes"),
            ("30", "30 minutes"),
            ("45", "45 minutes"),
            ("60", "1 hour"),
            # Add more options as needed
      ]
      duration = models.CharField(max_length=2, choices=DURATION_CHOICES)
      TYPE_CHOICES = [
            ("none", "None"),
            ("sauna", "Sauna"),
            ("ice_bath", "Ice Bath")
      ]
      type = models.CharField(max_length = 10, choices=TYPE_CHOICES, default = "none")
