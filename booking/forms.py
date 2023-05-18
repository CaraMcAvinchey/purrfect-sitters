from django import forms
from .models import Booking, Services
from phonenumber_field.formfields import PhoneNumberField
from bootstrap_datepicker_plus.widgets import DatePickerInput
import datetime


class DateInput(forms.DateInput):
    """
    This class gets the widget working to show a datepicker
    """
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """
    This class shows what inputs will be used in the form.
    Also gets the widgets for the time and date working.
    """
    class Meta:
        model = Booking

        fields = [
            'service_level', 'booking_date', 'phone',
            'special_instructions']

        widgets = {
            "booking_date": DatePickerInput(attrs={
                'min': datetime.date.today()+datetime.timedelta(days=0),
                'max': datetime.date.today()+datetime.timedelta(days=30)}),
        }
