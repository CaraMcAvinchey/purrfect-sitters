from django.db import models
from service.models import Services
from cat.models import Cat
from django.contrib.auth.models import User
from django.conf import settings
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField
import datetime


class Booking(models.Model):
    """
    Model for the information of each booking made on the website.
    """

    owner = models.ForeignKey(
        User,
        related_name="user",
        on_delete=models.CASCADE,
        )

    service_level = models.ForeignKey(
        Services,
        related_name="service_level",
        on_delete=models.PROTECT,
        null=True
        )

    booking_date = models.DateTimeField(null=True)

    date_created = models.DateTimeField(
        auto_now_add=True
    )

    cats = models.ManyToManyField(Cat)

    total = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    special_instructions = models.TextField(
        blank=True
    )

    phone = PhoneNumberField()

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
        current_user = None

        if hasattr(self, "user_id") and self.user_id is not None:
            current_user = self.user_id.id

        return Booking.objects\
            .filter(date=self.booking_date)\
            .filter(service=self.service_level)\
            .exclude(user_id=current_user)

    def save(self, *args, **kwargs):
        """
        A message if they try to book in the past.
        """
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot be in the past!")

        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return self.owner
