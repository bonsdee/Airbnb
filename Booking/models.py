from django.db import models
from django.contrib.auth.models import User

#  Owner Model
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

#  Guest Model
class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

#  Property Model
class Property(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField()
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#  Booking Model
class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ])

    def __str__(self):
        return f"Booking {self.id} - {self.guest.user.username} at {self.property.name}"

# Payment Model
class Payment(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[
        ('Credit Card', 'Credit Card'),
        ('PayPal', 'PayPal'),
        ('Bank Transfer', 'Bank Transfer')
    ])
    payment_status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed')
    ])
    transaction_date = models.DateField()

    def __str__(self):
        return f"Payment {self.id} - {self.guest.user.username} ({self.payment_status})"

class Review(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()  # Usually 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.guest.user.username} for {self.property.name}"

class Reserve(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    special_requests = models.TextField(blank=True)
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserver for Booking {self.booking.id} - {self.booking.guest.user.username}"
