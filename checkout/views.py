from django.shortcuts import render


def checkout(request):
    """
    View that returns the checkout page.
    """

    return render(request, 'checkout/checkout.html')
