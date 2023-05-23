from django.contrib import admin
from .models import Booking, Cat


@admin.register(Booking)
class CheckingAdmin(admin.ModelAdmin):

    readonly_fields = (
        'owner',
        'order_number',
        'payment_date',
    )

    fields = (
        'order_number',
        'payment_status',
        'street_address1',
        'town_or_city',
        'post_code'
    )

    list_display = [
        'owner',
        'order_number',
        'payment_status',
        'street_address1',
        'town_or_city',
        'post_code'
    ]

    ordering = ('-payment_date',)
