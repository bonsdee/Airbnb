from django.urls import path
from . import views  # Import views from the user app

urlpatterns = [
    path('', views.home, name='home'),
    path('properties/', views.property_list, name='property_list'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('api/properties/', views.api_properties, name='api_properties'),
]
