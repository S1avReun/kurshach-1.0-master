from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('new/', views.ProductCreateView.as_view(), name='product_new'),
    path('<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/delete/', views.ProductDelete, name='delete')
]