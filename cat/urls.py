from . import views
from django.urls import path
from .views import CatList


urlpatterns = [
    path('cat/', CatList.as_view(), name='cat'),
]
