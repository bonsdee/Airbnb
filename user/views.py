from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import  Profile


# Home Page View: it go to the the index
def home(request):
    return render(request, 'user/index.html')

"""
# Property List View: Retrieves all properties and displays them in a list.
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'user/property_list.html', {'properties': properties})
"""

"""
# Booking Detail View: Retrieves a specific booking by ID and displays its details.
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'user/booking_detail.html', {'booking': booking})
"""

"""
# API Endpoint for Properties: Returns a JSON response containing all properties.
def api_properties(request):
    properties = list(Property.objects.values())
    return JsonResponse({'properties': properties})
"""
# Login View: Authenticates the user using email and password.
from Booking.models import Owner  # Import the Owner model

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Email and password are required.")
            return redirect('login')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            authenticated_user = authenticate(request, username=user.username, password=password)

            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, f"Login successful! Welcome back, {authenticated_user.first_name}")

                # Redirect based on role (Owner → add_property)
                try:
                    Owner.objects.get(user=authenticated_user)
                    return redirect('add_property')
                except Owner.DoesNotExist:
                    return redirect('landing')

        messages.error(request, "Invalid email or password. Please try again.")
        return redirect('login')

    return render(request, 'user/login.html')


# Landing Page View: Displays the landing page for logged-in users.
@login_required
def landing_page(request):
    print(f"User authenticated: {request.user.is_authenticated}")  # Debugging ✅
    print(f"Current user: {request.user}")  # Debugging ✅
    return render(request, 'user/landing.html')


#Handles user sign-up and automatic login after registration.
from Booking.models import Owner  # Again, make sure it's imported

# Register View
def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')  # Get the role (owner or guest)

        # Check if email is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = full_name
        user.save()

        # Create a profile for the user with their role (owner or guest)
        Profile.objects.create(user=user, role=role)

        # Log in the user automatically after registration
        login(request, user)

        # If the role is 'owner', create an associated Owner instance
        if role.lower() == 'owner':
            Owner.objects.create(user=user, contact_number='')  # Create an Owner instance
            return redirect('add_property')  # Redirect to add_property page for owners

        # If the role is not 'owner' IT WILL GO TO LANDING PAGE
        messages.success(request, f"Registration successful! Welcome, {full_name}")
        return redirect('landing')

    return render(request, 'user/register.html')


# Logout View: Logs out the user and redirects to the home page.
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
