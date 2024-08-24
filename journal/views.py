from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import JournalEntry


class Journal(LoginRequiredMixin, ListView):
    template_name = "journal/journal.html"
    model = JournalEntry
    context_object_name = "journal_entries_list"

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user).order_by('-created_on')