from django import forms
from .models import Booking, Services
from phonenumber_field.formfields import PhoneNumberField
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
import datetime


class DateInput(forms.DateInput):
    """
    This class gets the widget working to show a datepicker
    """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    """
    This class gets the widget working to show a time picker
    """
    input_type = 'text'


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
            "booking_time": TimeInput(attrs={
                'class': 'timepicker'}),
        }
