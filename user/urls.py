from django.urls import path
from .views import home, login_view, register_view, property_list, booking_detail, api_properties, landing_page  # Import landing_page

urlpatterns = [
    path('', home, name='home'),
    path('properties/', property_list, name='property_list'),
    path('booking/<int:booking_id>/', booking_detail, name='booking_detail'),
    path('api/properties/', api_properties, name='api_properties'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('landing/', landing_page, name='landing'),  # Now properly imported
]
