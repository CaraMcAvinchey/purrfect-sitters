from . import views
from django.urls import path
from .views import CatList, CatDetail


urlpatterns = [
    path('cat/', CatList.as_view(), name='cat'),
    path('cat/<int:pk>', CatDetail.as_view(), name='cat_detail'),
]
