from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.TextField(max_length=50, default="Empty-name")
    price = models.DecimalField(max_digits=6,decimal_places=2, default=0)
    description = models.TextField(max_length=255, default="")
    discount = models.IntegerField(default=0)

class GymInfo(models.Model):
    name = models.TextField(max_length=255, default="")
    homeDescription = models.TextField(max_length=1000, default="")
