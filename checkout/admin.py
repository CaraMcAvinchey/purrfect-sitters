from django.contrib import admin
from .models import Booking, Cat, Checkout


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):

    readonly_fields = (
        'order_number',
        'payment_date',
    )

    fields = (
        'booking',
        'order_number',
        'payment_status',
        'street_address1',
        'town_or_city',
        'postcode'
    )

    list_display = [
        'order_number',
        'payment_status',
        'street_address1',
        'town_or_city',
        'postcode'
    ]

    ordering = ('-payment_date',)
