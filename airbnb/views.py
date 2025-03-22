# airbnb/views.py

from django.shortcuts import render

def login_view(request):
    return render(request, 'user/login')  # Make sure the path is correct
