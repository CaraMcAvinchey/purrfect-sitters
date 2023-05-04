from . import views
from django.urls import path
from .views import Home, ServiceList


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('services/', ServiceList.as_view(), name='services'),
]
