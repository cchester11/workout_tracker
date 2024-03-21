from django.core.exceptions import ValidationError
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
      VALID_DIFFICULTIES = [
            ("V0", "V0"),
            ("V1", "V1"),
            ("V2", "V2"),
            ("V3", "V3"),
            ("V4", "V4"),
            ("V5", "V5"),
            ("V6", "V6"),
            ("V7", "V7"),
            ("V8", "V8"),
            ("V9", "V9"),
            ("V10", "V10"),
      ]
      difficulty = models.CharField(
            max_length=5, choices=VALID_DIFFICULTIES
      )  # e.g., 'V1', 'V2', etc.

      def __str__(self):
            finished = 'no'

            if(self.completed):
                  finished = 'yes'
      
            return f'completed: {finished} - {self.difficulty}'
