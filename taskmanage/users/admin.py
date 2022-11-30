from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form =CustomUserCreationForm
    list_display = ['first_name', 'last_name', 'email', 'phone', 'username']
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)