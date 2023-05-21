from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .models import Booking, Services
from .forms import BookingForm
from cat.models import Cat
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
import datetime


@login_required
def booking(request):
    """
    The users can book a package for their cats.
    They get a message if their entered booking has already been booked.
    They get an email for confirmation.
    """
    form = BookingForm()
    booked = False
    error = None

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking_date = form.cleaned_data['booking_date']
            # check for booking in the past
            if booking_date < datetime.date.today():
                messages.error(request, "The date cannot be in the past!")
            else:
                booking_form = form.save(commit=False)
                booking_form.owner = request.user
            # check for double booking
                if not booking_form.is_timeslot_booked():
                    booking_form.save()
                    booked = True
                    messages.success(request, "Booking successful!")
                    return redirect('checkout')
                # error message for double booking
                else:
                    messages.error(request, "This date is already booked!")
        else:
            error = form.errors

    cats = Cat.objects.filter(owner=request.user)

    context = {
        'form': form,
        'booked': booked,
        "error": error,
        'cats': cats
        }

    return render(request, 'booking/booking.html', context)
