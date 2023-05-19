from . import views
from django.urls import path
from .views import CatList, CatDetail, CatCreateView


urlpatterns = [
    path('cat/', CatList.as_view(), name='cat'),
    path('cat/<int:pk>', CatDetail.as_view(), name='cat_detail'),
    path('cat/add/', CatCreateView.as_view(), name='add_cat'),
]
