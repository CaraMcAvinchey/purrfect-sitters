from django.shortcuts import render
from django.views import generic
from .models import Service


class Home(generic.TemplateView):
    model = Service
    template_name = 'index.html'


class ServiceList(generic.ListView):
    model = Service
    template_name = 'services.html'
