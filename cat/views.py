from django.shortcuts import render
from django.views import generic
from .models import Cat
from django.contrib.auth.mixins import LoginRequiredMixin


class CatList(generic.ListView):
    """
    View that displays the information profiles of
    each cat that a user owns.
    """
    model = Cat

    queryset = Cat.objects.all()
    template_name = 'cat/cat-profile.html'

    def queryset(self):
        return Cat.objects.filter(owner=self.request.user)


class CatDetail(generic.TemplateView):
    """
    View that displays the details of each cat.
    """
    model = Cat
    template_name = 'cat/cat-detail.html'