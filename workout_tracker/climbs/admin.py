from django.contrib import admin

# Register your models here.
from .models import Climbing, KilterBoarding, FreeClimb

admin.site.register(Climbing)
admin.site.register(KilterBoarding)
admin.site.register(FreeClimb)