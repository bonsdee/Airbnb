from django import forms
from django.contrib.auth.models import User
from .models import Guest, Owner, Property, Booking, Payment

# Guest Registration Form
class GuestRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Guest
        fields = ['contact_number']

    # If you want to register User as well, you can create a User in this form
    def save(self, commit=True):
        guest = super().save(commit=False)
        guest.username = self.cleaned_data['username']
        guest.set_password(self.cleaned_data['password'])
        if commit:
            guest.save()
        return guest

# Owner Registration Form
class OwnerRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Owner
        fields = ['contact_number']

    def save(self, commit=True):
        owner = super().save(commit=False)
        owner.username = self.cleaned_data['username']
        owner.set_password(self.cleaned_data['password'])
        if commit:
            owner.save()
        return owner

# Property Form
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'location', 'description', 'price_per_night']

    # Add any custom validations or field adjustments here if needed

# Booking Form
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['guest', 'property', 'check_in_date', 'check_out_date', 'total_price']

    # Add any validation logic here if needed (e.g., check that check_in < check_out)

# Payment Form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['guest', 'booking', 'amount', 'payment_method']

    # You can add custom validation here if required
