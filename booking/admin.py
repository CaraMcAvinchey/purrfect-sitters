from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    readonly_fields = (
        'owner',
        'cats',
        'date_created',
        # 'stripe_pid',
    )

    fields = (
        'owner',
        'cats',
        'service_level',
        'booking_date',
        'phone',
        'special_instructions',
    )

    list_display = [
        'owner',
        # 'cats',
        'service_level',
        'booking_date',
        'phone'
    ]

    ordering = ('-date_created',)
