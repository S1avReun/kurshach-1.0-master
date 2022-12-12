from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('cart_add/<int:id>', views.cart_add, name='cart_add'),
    path('cart_remove/<int:id>', views.cart_remove, name='cart_remove'),
]