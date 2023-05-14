from django.shortcuts import render
from django.views import generic
from .models import Booking


def booking(request):
    """
    To display the booking form so the user can book a room.
    """
    return render(request, 'booking/booking.html')

