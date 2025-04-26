from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Property, Booking, Payment, Guest, Owner
from .forms import GuestRegistrationForm, OwnerRegistrationForm, PropertyForm, BookingForm, PaymentForm
from datetime import date  # ✅ Add this!

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
        form = GuestRegistrationForm()
    return render(request, 'booking/guest_signup.html', {'form': form})

#  Owner Sign-up
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

#  List Properties
def property_listings(request):
    properties = Property.objects.all()
    return render(request, 'booking/property_listings.html', {'properties': properties})


# dets_ properts

def property_details(request, id):
    property = get_object_or_404(Property, pk=id)
    return render(request, 'booking/property_details.html', {'property': property})


#  Create Booking
# views.py

def create_booking(request, property_id):
    property = get_object_or_404(Property, id=property_id)  # Fetch property by ID
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.property = property
            booking.save()
            return redirect('payment')  # Redirect to payment form or confirmation page
    else:
        form = BookingForm()
    return render(request, 'booking/booking_form.html', {'form': form, 'property': property})


#  Make Payment
# views.py

def make_payment(request, booking_id):
    booking = Booking.objects.get(id=booking_id)  # Fetch the booking using the booking ID
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking  # Link payment to the booking
            payment.guest = booking.guest  # Link payment to the guest
            payment.payment_status = 'Pending'  # Set payment status to 'Pending'
            payment.save()
            booking.booking_status = 'Confirmed'  # After payment, change booking status to 'Confirmed'
            booking.save()
            return redirect('payment_success')
    else:
        form = PaymentForm()

    return render(request, 'booking/payment_form.html', {'form': form, 'booking': booking})

def payment_success(request):
    return render(request, 'booking/payment_success.html')


def book_property(request, id):
    property = get_object_or_404(Property, id=id)

    if request.user.is_authenticated:
        guest = get_object_or_404(Guest, user=request.user)

        # Create Booking directly (example dates, you can adjust)
        booking = Booking.objects.create(
            guest=guest,
            property=property,
            check_in_date=date.today(),  # Example: Today
            check_out_date=date.today(),  # Example: Today (or another logic)
            total_price=property.price_per_night,  # Assume 1 night
            booking_status='Pending'
        )

        return redirect('booking:make_payment', booking_id=booking.id)

    else:
        return redirect('login')  # If user not logged in, redirect to login


def payment(request, id):
    property = get_object_or_404(Property, id=id)
    if request.method == "POST":
        # pretend we process payment
        return render(request, 'booking/payment_success.html')
    return render(request, 'booking/payment_form.html', {'property': property})
