from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required


from .forms import CheckoutForm
from booking.models import Booking

# import stripe
# import json


@login_required()
def checkout(request, pk):
    """
    View that returns the checkout page.
    """
    checkout_form = CheckoutForm()

    if booking.owner != request.user:
        return HttpResponseForbidden(
            "You do not have permission \
                to access this booking.")

    if request.method == 'POST':
        booking = request.session.get('booking', {})
        checkout_form = CheckoutForm(request.POST)
        if checkout_form.is_valid():
            checkout = form.save()
            return redirect('checkout_success')
        else:
            messages.error(request, 'There was an error with your form.')
    else:
        checkout_form = CheckoutForm()
        booking = get_object_or_404(Booking, pk=pk)

    template = 'checkout/checkout.html'
    context = {
        'checkout_form': checkout_form,
        'booking': booking,
        'stripe_public_key': 'pk_test_51NC4ooHORblXBXM0yq6SxZajeH1HnLrVMJ7lpdhnf8z4ZGQMeMfSvphmyEzz7mepIohfoLUy9gEUxLRSzuruOON900bQydGd5W',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


def checkout_success(request):
    messages.success(request, "Payment successful!")
    return render(request, 'checkout/checkout_success.html')
