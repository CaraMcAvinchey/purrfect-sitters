from django.contrib import admin
from .models import Services
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Services)
class ServiceAdmin(SummernoteModelAdmin):

    list_display = (
        'service_name', 'service_description', 'price', 'service_choice')
    search_fields = ['service_name', 'service_choice'] 
