from django.contrib import admin
from .models import Owner, Guest, Property, Booking, Payment, Review, Reserve

admin.site.register(Owner)
admin.site.register(Guest)
admin.site.register(Property)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Reserve)


