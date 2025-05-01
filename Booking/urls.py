from django.urls import path
from .views import guest_signup, owner_signup, property_list, create_booking, make_payment, add_property

# Define a simple home view for the Booking app
from django.http import HttpResponse

def booking_home(request):
    return HttpResponse("Welcome to the Booking home page!")

urlpatterns = [
    path('', booking_home, name='booking_home'),  # <-- This handles /booking/
    path('properties/', property_list, name='property_list'),
    path('book/', create_booking, name='create_booking'),
    path('payment/', make_payment, name='make_payment'),
    path('add-property/', add_property, name='add_property'),

]
