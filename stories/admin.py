from django.contrib import admin
from .models import StoryEntry


@admin.register(StoryEntry)
class StoryEntryAdmin(admin.ModelAdmin):
    list_display = ('content', 'status', 'published_on')
    list_filter = ('status', 'published_on',)
    ordering = ('status', '-published_on')
