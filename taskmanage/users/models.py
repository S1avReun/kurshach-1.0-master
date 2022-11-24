from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    adress = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
