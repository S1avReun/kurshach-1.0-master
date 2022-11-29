from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    adress = models.CharField(max_length=100)
    phone = PhoneField(blank=True, help_text='Contact phone number')
