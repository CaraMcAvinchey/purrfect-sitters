import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from booking.models import Booking
from cat.models import Cat


class Checkout(models.Model):

    booking = models.ForeignKey(
            Booking,
            related_name="checkout",
            on_delete=models.PROTECT,
    )

    payment_date = models.DateTimeField(
        auto_now_add=True
    )

    ORDER_STATUS_CHOICES = [
        ('pending_payment', 'Pending'),
        ('payment_collected', 'Payment Collected'),
        ('payment_rejected', 'Payment Rejected'),
    ]

    payment_status = models.CharField(
        max_length=50,
        choices=ORDER_STATUS_CHOICES
    )

    street_address1 = models.CharField(
        max_length=80, null=False, blank=False
    )

    town_or_city = models.CharField(
        max_length=40, null=False, blank=False
    )

    postcode = models.CharField(
        max_length=20, null=True, blank=True
    )

    order_number = models.CharField(
        max_length=32, unique=True, editable=False
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
