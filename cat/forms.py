from django import forms
from .models import Cat
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from crispy_forms.helper import FormHelper


class AddCatForm(forms.ModelForm):
    """
    This form allows users to add a cat to their profile.
    It assists the user when typing their number with a place holder.
    If a user adds a cat, image field is required.
    """
    vet_contact = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(),
    )

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


class EditCatForm(forms.ModelForm):
    """
    This form allows users to edit a cat on their profile.
    If they are updating a cat, they can keep the existing image.
    """
    vet_contact = PhoneNumberField(
        widget=PhoneNumberPrefixWidget()
    )

    class Meta:
        model = Cat
        fields = [
            'cat_name', 'cat_age', 'cat_gender', 'cat_image',
            'cat_description', 'vet_contact'
        ]

        widgets = {
            'cat_image': forms.FileInput()
        }

    def __init__(self, *args, **kwargs):
        """
        Method which sets all fields to be editable and not required.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = False

    def clean_cat_image(self):
        """
        Method which returns the orginal image if a new one isn't provided.
        """
        cat_image = self.cleaned_data.get('cat_image')
        if self.instance.pk and not cat_image:
            return self.instance.cat_image
        return cat_image
