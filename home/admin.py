from django.contrib import admin
from .models import HomeContent


@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    """Admin interface for HomeContent model."""

    list_display = ["created_on", "introduction", "instructions"]
    ordering = ["-created_on"]
    search_fields = ["introduction", "instructions"]
    list_filter = ["created_on"]
