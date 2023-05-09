from django.shortcuts import render
from django.views import generic
from .models import Cat


class CatList(generic.ListView):
    """
    View that displays the information profiles of 
    each cat that a user owns.
    """
    model = Cat

    queryset = Cat.objects.all()
    template_name = 'cat/cat-profile.html'
