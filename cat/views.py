from django.shortcuts import render
from django.views import generic
from .models import Cat
from .forms import AddCatForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class CatList(generic.ListView):
    """
    View that displays the information profiles of
    each cat that a user owns.
    """
    model = Cat
    template_name = 'cat/cat_profile.html'

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)


class CatDetail(generic.DetailView):
    """
    View that displays the details of each cat.
    """
    model = Cat
    template_name = 'cat/cat_detail.html'


class CatCreateView(LoginRequiredMixin, CreateView):
    """
    View that allows the user to add a cat to their profile.
    """
    form_class = AddCatForm
    template_name = 'cat/add_cat.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        super().form_valid(form)
        messages.success(self.request, "Added a new cat!")
        return HttpResponseRedirect(self.get_success_url()) 

    def get_success_url(self):
        return reverse('cat')
