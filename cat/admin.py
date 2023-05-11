from django.contrib import admin
from .models import Cat
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Cat)
class CatAdmin(SummernoteModelAdmin):

    list_display = (
        'id', 'owner', 'cat_name', 'cat_age', 'cat_gender', 'cat_image', 'cat_description', 'vet_contact', 'profile_updated')
    search_fields = ['cat_name', 'owner']
