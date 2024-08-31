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
            "mood": "How do you feel today?",
            "day_description": "Describe your day in one sentence",
            "content": "Journal entry",
            "grateful_for": "What are you grateful for today?",
            "improve_on": "What should you improve on?",
            "is_public": "Share your entry with the community?",
        }
