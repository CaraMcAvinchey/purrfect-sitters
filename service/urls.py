from . import views
from django.urls import path
from .views import ServiceList


urlpatterns = [
    path('services/', ServiceList.as_view(), name='services'),
]
