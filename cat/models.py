from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


class Cat(models.Model):
    """
    Model for the basic information stored about each cat.
    This helps the cat sitter know more about the cats booked.
    """

    class Meta:
        verbose_name_plural = 'Cat Profiles'

    owner = models.ForeignKey(
        User,
        related_name="cats",
        on_delete=models.CASCADE,
        )

    cat_name = models.CharField(
        max_length=50
    )

    CAT_AGES = [
        ("3 years and younger", "3 years and younger"),
        ("4-9 years old", "4-9 years old"),
        ("10-15 years old", "10-15 years old"),
        ("Above 16 years old", "Above 16 years old"),
    ]

    cat_age = models.CharField(
        max_length=50,
        choices=CAT_AGES,
    )

    GENDER_CHOICES = [
        ("Female", "Female"),
        ("Male", "Male"),
    ]

    cat_gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    cat_image = models.ImageField(
        null=True,
        blank=True
    )

    cat_description = models.TextField(
        null=True,
        blank=True
    )

    vet_contact = PhoneNumberField()

    profile_updated = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        #  Returns a string of name of the service
        return f"{self.cat_name}"
