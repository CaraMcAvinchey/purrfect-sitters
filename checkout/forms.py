from django import forms
from .models import Checkout, Cat
from django.core.exceptions import ValidationError
import datetime


class CheckoutForm(forms.ModelForm):
    """
    This class shows what inputs will be used in the form.
    Also gets the widgets for form placeholders.
    """
    class Meta:
        model = Checkout
        fields = ('street_address1', 'town_or_city', 'postcode')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'street_address1': 'Street Address',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
        }

        self.fields['street_address1'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
