from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Guest, Owner, Property


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
