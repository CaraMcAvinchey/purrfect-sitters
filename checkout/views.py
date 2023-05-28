from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .forms import CheckoutForm
from booking.models import Booking

import stripe
# import json


@login_required()
def checkout(request, pk):
    """
    View that returns the checkout page.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    booking = get_object_or_404(Booking, pk=pk)

    if booking.owner != request.user:
        return HttpResponseForbidden(
            "You do not have permission \
                to access this booking.")

    stripe_total = int(booking.total)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    checkout_form = CheckoutForm()

    # if request.method == 'POST':
    #     checkout_form = CheckoutForm(request.POST)
    #     if checkout_form.is_valid():
    #         checkout = checkout_form.save(commit=False)
    #         checkout.booking = booking
    #         checkout.save()
    #         return redirect('checkout_success')
    #     else:
    #         messages.error(request, 'There was an error with your form.')
    # else:
    #     checkout_form = CheckoutForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'booking': booking,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


# def checkout_success(request):
#     messages.success(request, "Payment successful!")
#     return render(request, 'checkout/checkout_success.html')
