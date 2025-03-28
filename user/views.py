from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from .models import Property, Booking


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
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Ensure email and password fields are filled
        if not email or not password:
            messages.error(request, "Email and password are required.")
            return redirect('login')

        try:
            # Retrieve the user by email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            # Authenticate using the found user's username
            authenticated_user = authenticate(request, username=user.username, password=password)

            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, f"Login successful! Welcome back, {authenticated_user.first_name}")
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
def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        # Create a user with email as the username
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = full_name
        user.save()

        # Log in the new user
        login(request, user)
        messages.success(request, f"Registration successful! Welcome, {full_name}")
        return redirect('home')

    return render(request, 'user/register.html')


# Logout View: Logs out the user and redirects to the home page.
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
