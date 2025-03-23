from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Property, Booking, Payment, Guest, Owner
from .forms import GuestRegistrationForm, OwnerRegistrationForm, PropertyForm, BookingForm, PaymentForm

# 👤 Guest Sign-up
def guest_signup(request):
    if request.method == 'POST':
        form = GuestRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            guest = Guest.objects.create(user=user, contact_number=form.cleaned_data['contact_number'])
            login(request, user)
            return redirect('home')
    else:
        form = GuestRegistrationForm()
    return render(request, 'booking/guest_signup.html', {'form': form})

# 🏠 Owner Sign-up
def owner_signup(request):
    if request.method == 'POST':
        form = OwnerRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            owner = Owner.objects.create(user=user, contact_number=form.cleaned_data['contact_number'])
            login(request, user)
            return redirect('home')
    else:
        form = OwnerRegistrationForm()
    return render(request, 'booking/owner_signup.html', {'form': form})

# 🏡 List Properties
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'booking/property_list.html', {'properties': properties})

# 📆 Create Booking
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form})

# 💳 Make Payment
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PaymentForm()
    return render(request, 'booking/payment_form.html', {'form': form})
