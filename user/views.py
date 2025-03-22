from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Property, Booking


def home(request):
    return render(request, 'user/index.html')


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'user/property_list.html', {'properties': properties})


def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'user/booking_detail.html', {'booking': booking})


def api_properties(request):
    properties = list(Property.objects.values())
    return JsonResponse({'properties': properties})
