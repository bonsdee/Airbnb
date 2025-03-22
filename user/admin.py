from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Guest, Owner, Property, Booking, Payment


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_number')
    search_fields = ('name', 'email')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_number')
    search_fields = ('name', 'email')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_night', 'owner')
    search_fields = ('name', 'location')
    list_filter = ('owner',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('guest', 'property', 'check_in_date', 'check_out_date', 'total_price', 'booking_status')
    search_fields = ('guest__name', 'property__name')
    list_filter = ('booking_status', 'check_in_date', 'check_out_date')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('guest', 'booking', 'amount', 'payment_method', 'payment_status', 'transaction_date')
    search_fields = ('guest__name', 'booking__id')
    list_filter = ('payment_status', 'payment_method')
