from . import views
from django.urls import path
from .views import booking, my_bookings


urlpatterns = [
    path('booking/', booking, name='booking'),
    path('booking/my_bookings/', views.my_bookings, name='my_bookings'),
]
