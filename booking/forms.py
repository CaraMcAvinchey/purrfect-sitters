from django import forms
from .models import Booking, Services
from phonenumber_field.formfields import PhoneNumberField
import datetime


class BookingForm(forms.ModelForm):
    """
    This class shows what inputs will be used in the form.
    Also gets the widgets for the time and date working.
    """
    class Meta:
        model = Booking

        fields = [
            'service_level', 'booking_date', 'cats', 'phone',
            'special_instructions']
