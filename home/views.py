from django.shortcuts import render
from django.views.generic.base import TemplateView


def index(request):
    """
    View that returns the home page.
    """

    return render(request, 'home/index.html')


class Page400(TemplateView):
    """
    View that returns 400 error page.
    """
    template_name = '400.html'


class Page403(TemplateView):
    """
    View that returns 403 error page.
    """
    template_name = '403.html'


class Page404(TemplateView):
    """
    View that returns 404 error page.
    """
    template_name = '404.html'


class Page500(TemplateView):
    """
    View that returns 500 error page.
    """
    template_name = '500.html'
