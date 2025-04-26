from django.urls import path
from . import views
from .views import home, login_view, register_view, landing_page,property_listings

urlpatterns = [
    path('', home, name='home'),
   # path('properties/', property_list, name='property_list'),
   # path('booking/<int:booking_id>/', booking_detail, name='booking_detail'),
   # path('api/properties/', api_properties, name='api_properties'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('landing/', landing_page, name='landing'),
    path('property-listings/', views.property_listings, name='property_list'),
    path('hosting/', views.hosting_dashboard, name='hosting_dashboard'),
    path('hosting/add-property/', views.add_property, name='add_property'),


]