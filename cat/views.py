from django.shortcuts import render, get_list_or_404, reverse
from django.views import generic
from .models import Cat
from .forms import AddCatForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
    This includes additional information not on the cat cards.
    """
    model = Cat
    template_name = 'cat/cat_detail.html'


class CatCreateView(LoginRequiredMixin, CreateView):
    """
    View that allows the user to add a cat to their profile.
    The user must add a picture of the cat they're trying to add.
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


class EditCat(LoginRequiredMixin, UpdateView):
    """
    View that allows a logged in user to edit a cat in their profile.
    """
    model = Cat
    form_class = AddCatForm
    template_name = 'cat/edit_cat.html'
    success_url = reverse_lazy('cat:cat_list')

    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, "You've edited this cat!")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        """
        Upon success returns user to the cat detail page.
        """
        return reverse("cat_detail", kwargs={"pk": self.object.pk})


class DeleteCat(LoginRequiredMixin, DeleteView):
    """
    View that allows logged in users to delete a cat from their profile.
    The user us prompted with a warning.
    """
    model = Cat
    template_name = 'cat/delete_cat.html'

    def delete(self, request, *args, **kwargs):
        return super(DeleteCat, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        CatDetail.cat_deleted = True
        messages.success(self.request, 'You have deleted a cat from your profile!')
        return reverse_lazy("cat")
