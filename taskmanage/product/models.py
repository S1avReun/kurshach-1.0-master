from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True, verbose_name='Изображение')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list')