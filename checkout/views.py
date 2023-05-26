from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings


from .forms import CheckoutForm
from booking.models import Booking

# import stripe
# import json


def checkout(request):
    """
    View that returns the checkout page.
    """
    checkout_form = CheckoutForm()

    if request.method == 'POST':
        booking = request.session.get('booking')
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            checkout = form.save()
            return redirect('checkout_success')
        else:
            messages.error(request, 'There was an error with your form.')
    else:
        checkout_form = CheckoutForm()

    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
    }

    return render(request, template, context)


def checkout_success(request):
    messages.success(request, "Payment successful!")
    return render(request, 'checkout/checkout_success.html')
