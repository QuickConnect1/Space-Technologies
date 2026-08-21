from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('work/', views.work, name='work'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]