from django.urls import path

from .views import weather_view, contact_view

urlpatterns = [
    path('', weather_view, name='weather_home'),
    path('contact/', contact_view, name='contact'),
]