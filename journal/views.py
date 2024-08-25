from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import JournalEntry
from .forms import JournalEntryForm


class Journal(LoginRequiredMixin, ListView):
    """
    View that displays a list of journal entries for the logged-in user.
    """

    template_name = "journal/journal.html"
    model = JournalEntry
    context_object_name = "journal_entries_list"

    def get_queryset(self):
        """Return the list of journal entries for the logged-in user."""
        return (
            JournalEntry.objects
            .filter(user=self.request.user)
            .order_by('-created_on')
        )


class AddJournalEntry(LoginRequiredMixin, CreateView):
    """
    View for creating a new journal entry.
    """

    template_name = "journal/add_journal_entry.html"
    model = JournalEntry
    form_class = JournalEntryForm
    success_url = "/journal/"

    def form_valid(self, form):
        """Process the form data and save the journal entry."""
        form.instance.user = self.request.user

        # Save the journal entry first
        response = super().form_valid(form)
        messages.success(self.request, "Journal Entry Added!")

        # After saving, check if it's public and publish as a story
        if form.instance.is_public:
            form.instance.publish_as_story()

        return response
