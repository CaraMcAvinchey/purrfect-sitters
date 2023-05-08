from django.shortcuts import render
from django.views import generic
from .models import Services


class ServiceList(generic.ListView):
    """
    View that displays the service name, description and price
    """
    model = Services

    queryset = Services.objects.all()
    template_name = 'service/services.html'
