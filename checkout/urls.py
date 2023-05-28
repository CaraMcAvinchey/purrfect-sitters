from django.urls import path
from . import views

urlpatterns = [
    # path('checkout/', views.checkout, name='checkout'),
    path('checkout/<str:pk>/', views.checkout, name='checkout'),
    path('checkoutsuccess/', views.checkout_success, name='checkout_success'),
]
