from django import forms
from .models import Cat
from phonenumber_field.formfields import PhoneNumberField


class AddCatForm(forms.ModelForm):
    """
    This form allows users to add a cat to their profile.
    """
    class Meta:
        model = Cat
        fields = [
            'cat_name', 'cat_age', 'cat_gender', 'cat_image',
            'cat_description', 'vet_contact']
