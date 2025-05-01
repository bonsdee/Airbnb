from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Property, Booking, Payment, Guest, Owner
from .forms import GuestRegistrationForm, OwnerRegistrationForm, PropertyForm, BookingForm, PaymentForm
from django.db import connection


# Guest Sign-up
def guest_signup(request):
    if request.method == 'POST':
        form = GuestRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            guest = Guest.objects.create(user=user, contact_number=form.cleaned_data['contact_number'])
            login(request, user)
            return redirect('home')
    else:
        form = GuestRegistrationForm()  # Empty form for GET requests
    return render(request, 'booking/guest_signup.html', {'form': form})

# Owner Sign-up
def owner_signup(request):
    if request.method == 'POST':
        form = OwnerRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            owner = Owner.objects.create(user=user, contact_number=form.cleaned_data['contact_number'])
            login(request, user)
            return redirect('add_property')  # <-- go to add_property
    else:
        form = OwnerRegistrationForm()  # Empty form for GET requests
    return render(request, 'booking/owner_signup.html', {'form': form})

# List Properties
# This view displays all available properties in the system.
# It fetches all the properties from the database and renders them on the property_list template.
def property_list(request):
    properties = Property.objects.all()  # Fetch all properties
    return render(request, 'booking/property_list.html', {'properties': properties})

# Create Booking
# This view allows users to create a booking. It processes the booking form and saves the data to the database.
# After a successful booking, the user is redirected to the property list page.
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the booking to the database
            return redirect('property_list')  # Redirect to the property list after booking
    else:
        form = BookingForm()  # Empty form for GET requests
    return render(request, 'booking/booking_form.html', {'form': form})

# Make Payment
# This view handles the payment process. After the payment form is submitted, the payment is saved to the database.
# After successful payment, the user is redirected to the property list.
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the payment data to the database
            return redirect('property_list')  # Redirect to the property list after payment
    else:
        form = PaymentForm()  # Empty form for GET requests
    return render(request, 'booking/payment_form.html', {'form': form})

# Add Property (for owners only)
# This view allows owners to add properties. It checks if the logged-in user is an owner.
# If the user is not an owner, they are redirected to the home page with an error message.
# If the user is an owner, they can submit the property form to add a new property.
@login_required
def add_property(request):
    try:
        owner = Owner.objects.get(user=request.user)
    except Owner.DoesNotExist:
        messages.error(request, "Only owners can add properties.")
        return redirect('home')

    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price_per_night']

            try:
                with connection.cursor() as cursor:
                    # Call the stored procedure
                    cursor.callproc('AddProperty', [
                        name,
                        location,
                        description,
                        price,
                        owner.id
                    ])
                messages.success(request, "Property added successfully using stored procedure.")
                return redirect('add_property')  # Redirect to clear the form after success
            except Exception as e:
                messages.error(request, f"Database Error: {e}")
    else:
        form = PropertyForm()

    return render(request, 'booking/add_property.html', {'form': form})