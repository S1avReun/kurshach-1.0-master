from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.CharField(max_length=60, verbose_name='Email')
    adress = models.CharField(max_length=100, verbose_name='Адрес')
    phone = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='Номер телефона')
