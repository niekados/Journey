from django.urls import path
from .views import (
    Journal,
    AddJournalEntry,
    JournalDetail,
    delete_journal_entry
)

urlpatterns = [
    path("", Journal.as_view(), name="journal"),
    path("add/", AddJournalEntry.as_view(), name="add_journal_entry"),
    path("<int:pk>/", JournalDetail.as_view(), name="journal_detail"),
    path(
        "delete/<int:pk>/",
        delete_journal_entry,
        name="delete_journal_entry"
    ),
]
