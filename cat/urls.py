from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CatList, CatDetail, CatCreateView, EditCat, DeleteCat


urlpatterns = [
    path('cat/', CatList.as_view(), name='cat'),
    path('cat/<int:pk>', CatDetail.as_view(), name='cat_detail'),
    path('cat/add/', login_required(CatCreateView.as_view()), name='add_cat'),
    path('cat/edit/<int:pk>/', login_required(EditCat.as_view()), name='edit_cat'),
    path('cat/delete<int:pk>/', login_required(DeleteCat.as_view()), name='delete_cat'),
]
