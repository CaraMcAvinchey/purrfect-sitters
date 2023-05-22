from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    readonly_fields = (
        'owner',
        'cats',
        'date_created',
        'booking_number'
    )

    fields = (
        'booking_number',
        'owner',
        'cats',
        'service_level',
        'booking_date',
        'phone',
        'special_instructions',
        'total'
    )

    list_display = [
        'owner',
        'service_level',
        'booking_date',
        'total',
        'phone',
        'booking_number'
    ]

    ordering = ('-date_created',)
