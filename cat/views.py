from django.shortcuts import render, get_list_or_404, reverse
from django.views import generic
from .models import Cat
from .forms import AddCatForm, EditCatForm
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


class CatList(LoginRequiredMixin, generic.ListView):
    """
    View that displays the information profiles of
    each cat that a user owns in summary cards.
    """
    model = Cat
    template_name = 'cat/cat_profile.html'

    def get_queryset(self):
        return Cat.objects.filter(owner=self.request.user)


class CatDetail(LoginRequiredMixin, generic.DetailView):
    """
    View that displays the details of each cat.
    This includes additional information not on the cat cards.
    """
    model = Cat
    template_name = 'cat/cat_detail.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Method to validate owner against logged in user.
        """
        cat = self.get_object()
        if cat.owner != request.user:
            raise PermissionDenied()

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)


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
    form_class = EditCatForm
    template_name = 'cat/edit_cat.html'
    success_url = reverse_lazy('cat:cat_list')

    def form_valid(self, form):
        """
        Method to validate owner against logged in user.
        """
        cat = self.get_object()
        if cat.owner != self.request.user:
            return PermissionDenied

        super().form_valid(form)
        messages.success(self.request, "You've edited this cat!")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        return reverse("cat_detail", kwargs={"pk": self.object.pk})

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)


class DeleteCat(LoginRequiredMixin, DeleteView):
    """
    View that allows logged in users to delete a cat from their profile.
    The user us prompted with a warning.
    """
    model = Cat
    template_name = 'cat/delete_cat.html'

    def delete(self, request, *args, **kwargs):
        """
        Method to validate owner against logged in user.
        """
        cat = self.get_object()
        if cat.owner != request.user:
            return PermissionDenied()
        return super(DeleteCat, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        CatDetail.cat_deleted = True
        messages.success(
            self.request, 'You have deleted a cat from your profile!')
        return reverse_lazy("cat")

    def handle_no_permission(self):
        return render(self.request, '403.html', status=403)
