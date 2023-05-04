from django.db import models


class Services(models.Model):
    """
    Model for the information about the services on offer.
    """

    service_name = models.CharField(
        max_length=100
    )

    service_description = models.TextField(
        max_length=300
    )

    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    SERVICE_CHOICES = [
        ("1", "Package 1 - 30 minutes"),
        ("2", "Package 2 - 60 minutes"),
    ]

    service_choice = models.IntegerField(
        choices=SERVICE_CHOICES,
        default=1,
        null=True
    )

    def __str__(self):
        #  Returns a string of name of the service
        return f"{self.service_name}"
