from django import forms
from Booking.models import Property  # ✅ Because Property is from Booking app

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'location', 'description', 'price_per_night']
