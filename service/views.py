from django.shortcuts import render
from django.views import generic
from .models import Services


class Home(generic.TemplateView):
    model = Services
    template_name = 'index.html'


class ServiceList(generic.ListView):
    model = Services
    template_name = 'services.html'
