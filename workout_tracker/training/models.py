from django.db import models
from core.models import Workout

# Create your models here.
class Training(models.Model):
      workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
      campus_boarding = models.BooleanField()
      hanging = models.BooleanField()