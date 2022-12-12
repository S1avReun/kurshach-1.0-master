from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', views.aboutPageView, name='about'),
    path('contacts/', views.contactsPageView, name='contacts'),
    path('prices/', views.pricesPageView, name='prices'),
]