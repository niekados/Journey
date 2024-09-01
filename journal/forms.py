from django import forms
from .models import JournalEntry


class JournalEntryForm(forms.ModelForm):
    """
    A form for creating and updating journal entries.
    """

    class Meta:
        model = JournalEntry
        fields = [
            "mood",
            "day_description",
            "content",
            "grateful_for",
            "improve_on",
            "is_public",
        ]
        labels = {
            "mood": "How do I feel today?",
            "day_description": "Sum up my day in 5 words.",
            "content": "My day's story",
            "grateful_for": "What am I thankful for today?",
            "improve_on": "How can I be better tomorrow?",
            "is_public": "Share this entry with the community?",
        }
