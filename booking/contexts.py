from decimal import Decimal
from django.conf import settings
from booking.forms import BookingForm


def booking_contents(request):

    booking_items = []
    booking_total = 0

    context = {
        'booking_items': booking_items,
        'booking_total': booking_total
    }

    return context
