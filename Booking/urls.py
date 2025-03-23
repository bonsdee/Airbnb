from django.urls import path
from .views import guest_signup, owner_signup, property_list, create_booking, make_payment

urlpatterns = [
    path('guest-signup/', guest_signup, name='guest_signup'),
    path('owner-signup/', owner_signup, name='owner_signup'),
    path('properties/', property_list, name='property_list'),
    path('book/', create_booking, name='create_booking'),
    path('payment/', make_payment, name='make_payment'),
]
