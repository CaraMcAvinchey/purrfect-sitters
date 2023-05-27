from django.db import models


class Services(models.Model):
    """
    Model for the information about the services on offer.
    Includes service name, description, price and package choice.
    """

    service_name = models.CharField(
        max_length=100,
        verbose_name="Service Name"
    )

    service_description = models.TextField(
        max_length=400,
        verbose_name="Service Description"
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Package Price"
    )

    SERVICE_CHOICES = [
        ("1", "30 minutes"),
        ("2", "60 minutes"),
    ]

    service_choice = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
        null=True,
        verbose_name="Service Choice"
    )

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.service_name}"
