from django.urls import path
from .views import Journal, AddJournalEntry

urlpatterns = [
    path("", Journal.as_view(), name="journal"),
    path("add/", AddJournalEntry.as_view(), name="add_journal_entry"),
]
