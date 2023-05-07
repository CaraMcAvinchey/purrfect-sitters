from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('400', views.Page400.as_view(), name='400'),
    path('403', views.Page403.as_view(), name='403'),
    path('404', views.Page404.as_view(), name='404'),
    path('500', views.Page500.as_view(), name='500'),
]