from django.urls import path
from . import views

app_name = 'booking'
from .views import guest_signup, owner_signup, property_listings, create_booking, make_payment

# Define a simple home view for the Booking app
from django.http import HttpResponse

def booking_home(request):
    return HttpResponse("Welcome to the Booking home page!")

urlpatterns = [
    path('', booking_home, name='booking_home'),  # <-- This handles /booking/
    path('guest-signup/', guest_signup, name='guest_signup'),
    path('owner-signup/', owner_signup, name='owner_signup'),
    path('property-listings/', views.property_listings, name='property_listings'),
    path('payment/', make_payment, name='make_payment'),
    path('book_property/<int:property_id>/', views.create_booking, name='create_booking'),
    path('make_payment/<int:booking_id>/', views.make_payment, name='make_payment'),
    path('payment_success/', views.payment_success, name='payment_success'),
    path('property-details/<int:id>/', views.property_details, name='property_details'),
    path('book/<int:id>/', views.book_property, name='book_property'),
    path('payment/<int:id>/', views.payment, name='payment'),



]
