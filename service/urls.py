from . import views
from django.urls import path
from .views import ServiceList


urlpatterns = [
    path('service/', ServiceList.as_view(), name='services'),
]
