from django.contrib import admin
from .models import HomeContent


@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = [
        'created_on',
        'introduction',
        'instructions'
    ]
    ordering = ['-created_on']
