from django.db import models
from service.models import Services
from cat.models import Cat
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
import datetime
import decimal
import uuid


class Booking(models.Model):
    """
    Model for the information of each booking made on the website.
    """

    owner = models.ForeignKey(
        User,
        related_name="bookings",
        on_delete=models.CASCADE,
        )

    service_level = models.ForeignKey(
        Services,
        related_name="service_level",
        on_delete=models.PROTECT,
        null=True
        )

    booking_date = models.DateField(null=True)

    date_created = models.DateTimeField(
        auto_now_add=True
    )

    cats = models.ManyToManyField(Cat)

    total = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    special_instructions = models.TextField(
        blank=True
    )

    phone = PhoneNumberField()

    booking_number = models.CharField(
        max_length=32, null=True, blank=True, editable=False)

    @property
    def number_cats(self):
        """
        Get the number of cats associated with the booking
        """
        return len(self.cats)

    def is_timeslot_booked(self):
        """
        This ensures that when the user is trying to update
        the booking, it is the user that the booking belongs to.
        Makes sure the user can't double book.
        """
        current_user = self.owner

        return Booking.objects\
            .filter(owner=current_user, booking_date=self.booking_date).exists()

    def calculate_total(self):
        """
        Calculate the total based on the service level chosen
        and the number of cats.If the cats associated with the user
        are greater than 3 there is a surcharge.
        """
        base_price = self.service_level.price
        cat_count = self.cats.count()
        extra_cat_fee = 10 * (cat_count - 3) if cat_count > 3 else 0
        total = decimal.Decimal(base_price) + decimal.Decimal(extra_cat_fee)
        return total

    def _generate_booking_number(self):
        """
        Generate a random, unique order number using UUID
        Prepended with an _ to indicate it's a private method
        (only be used inside this class)
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Save the booking, calculate the total.
        """
        if isinstance(self.booking_date, datetime.datetime):
            self.booking_date = self.booking_date.date()

        if not self.booking_number:
            self.booking_number = self._generate_booking_number()

        super().save(*args, **kwargs)
        self.total = self.calculate_total()
        self.cats.set(self.cats.all())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking #{self.booking_number} - {self.owner} - {self.booking_date}"
