from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Create your models here.


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(validators=[validators.MinValueValidator(18)])

    def __str__(self):
        return f"Driver {self.user} with age {self.age}"


class Passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(validators=[validators.MinValueValidator(18)])

    def __str__(self):
        return f"Passenger {self.user} with age {self.age}"
