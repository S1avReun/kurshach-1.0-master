from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    list_filter = ['name', 'price', 'description']
    list_editable = ['price']
admin.site.register(Product, ProductAdmin)
