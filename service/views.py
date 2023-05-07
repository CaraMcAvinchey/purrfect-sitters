from django.shortcuts import render
from django.views import generic
from .models import Services


class ServiceList(generic.ListView):
    model = Services
    template_name = 'service/services.html'
