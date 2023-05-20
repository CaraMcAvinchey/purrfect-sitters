from django import forms
from .models import Cat
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class AddCatForm(forms.ModelForm):
    """
    This form allows users to add a cat to their profile.
    It assists the user when typing their number with a place holder.
    If a user adds a cat, image field is required.
    If they are updating a cat, they can keep the existing image.
    """
    vet_contact = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(
            attrs={'placeholder': '079 1138 9779'}))

    class Meta:
        model = Cat
        fields = [
            'cat_name', 'cat_age', 'cat_gender', 'cat_image',
            'cat_description', 'vet_contact'
        ]

        widgets = {
            'cat_image': forms.FileInput(attrs={'required': True})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            # Set initial value for cat_image field when editing a cat.
            self.fields['cat_image'].initial = instance.cat_image

    def clean_cat_image(self):
        cat_image = self.cleaned_data.get('cat_image')
        if self.instance.pk and not cat_image:
            # The image field is not required when editing an exisiting cat
            # If left blank, it will keep the existing image.
            return self.instance.cat_image
        return cat_image
