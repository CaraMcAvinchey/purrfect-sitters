from . import views
from django.urls import path
from .views import ServiceList


urlpatterns = [
    path('', ServiceList.as_view(), name='services'),
]
