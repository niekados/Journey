from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import JournalEntry
from .forms import JournalEntryForm


class Journal(LoginRequiredMixin, ListView):
    """
    View that displays a list of journal entries for the logged-in user.
    """

    template_name = "journal/journal.html"
    model = JournalEntry
    context_object_name = "journal_entries_list"
    paginate_by = 8

    def get_queryset(self, **kwargs):
        """
        Filter the queryset to include the logged-in user's journal entries
        and provide search functionality.
        """
        query = self.request.GET.get("journal_query")

        # Filter the user's own entries
        queryset = JournalEntry.objects.filter(user=self.request.user)

        # Apply search filters if a search query is provided
        if query:
            queryset = queryset.filter(
                Q(day_description__icontains=query)
                | Q(content__icontains=query)
                | Q(grateful_for__icontains=query)
                | Q(improve_on__icontains=query)
            )

        # Order the results by creation date, most recent first
        return queryset.order_by("-created_on")


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
        messages.success(self.request, "Journal entry added!")

        # After saving, check if it's public and publish as a story
        if form.instance.is_public:
            form.instance.publish_as_story()

        return response


class JournalDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """
    View for displaying detailed journal entry.
    """

    template_name = "journal/journal_detail.html"
    model = JournalEntry
    context_object_name = "journal_entry_detail"

    def test_func(self):
        # Ensure that only the owner can view their journal entry
        return self.request.user == self.get_object().user


@login_required
def delete_journal_entry(request, pk):
    """
    Delete a journal entry based on its primary key (pk).
    """
    # Get the journal entry or return a 404 if it doesn't exist
    journal_entry = get_object_or_404(JournalEntry, pk=pk)

    if request.method == "POST":
        # Check if the logged-in user is the owner of the journal entry
        if journal_entry.user == request.user:
            # Delete the journal entry
            journal_entry.delete()
            messages.success(request, "Journal entry deleted!")
            return redirect("journal")
        else:
            # Add an error message if the user doesn't have permission
            messages.error(
                request,
                "You are not authorized to delete this journal entry!"
            )
            return redirect("journal")
    else:
        # If method is GET, confirm that the logged-in user is the entry owner
        if journal_entry.user == request.user:
            # Render the confirmation template
            return render(
                request,
                "journal/journal_entry_confirm_delete.html",
                {"journal_entry": journal_entry},
            )
        else:
            # Add an error message if the user isn't entry owner
            messages.error(
                request, "You are not authorized to delete this journal entry!"
            )
            return redirect("journal")


@login_required
def edit_journal_entry(request, pk):
    """
    Edit a journal entry based on its primary key (pk).
    """
    # Get the journal entry or return a 404 if it doesn't exist
    journal_entry = get_object_or_404(JournalEntry, pk=pk)

    # Check if the logged-in user is not the owner of the journal entry
    if journal_entry.user != request.user:
        messages.error(
            request,
            "You are not authorized to edit this journal entry."
            )
        return redirect("journal")

    # Process the form data if the request method is POST
    if request.method == "POST":
        form = JournalEntryForm(data=request.POST, instance=journal_entry)

        if form.is_valid():
            # Save the updated journal entry
            form.save()
            messages.success(request, "Journal entry updated!")

            # Publish or unpublish the entry based on its current status
            if journal_entry.is_public:
                journal_entry.publish_as_story()
            else:
                journal_entry.unpublish_story()

            return redirect("journal")
        else:
            messages.error(
                request,
                "There was an error while updating the Journal Entry"
            )
    else:
        # Render the form with the current journal entry data for a GET request
        form = JournalEntryForm(instance=journal_entry)

    return render(request, "journal/edit_journal_entry.html", {"form": form})
