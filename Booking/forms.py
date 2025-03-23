from django import forms
from django.contrib.auth.models import User
from .models import Guest, Owner, Property, Booking, Payment

# 👤 Guest Registration Form
class GuestRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Guest
        fields = ['contact_number']

# 🏠 Owner Registration Form
class OwnerRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Owner
        fields = ['contact_number']

# 🏡 Property Form
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'location', 'description', 'price_per_night']

# 📆 Booking Form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['property', 'check_in_date', 'check_out_date']

# 💳 Payment Form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_method']
