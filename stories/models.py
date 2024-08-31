from django.db import models
from journal.models import JournalEntry

STATUS = (
    (0, "Pending"),
    (1, "Published"),
)


class StoryEntry(models.Model):
    """
    Represents a story shared by a user. Each story is associated
    with a specific journal entry and can be published or pending
    approval.

    Attributes:
        journal_entry (OneToOneField): A relationship with JournalEntry.
        content (TextField): The content of the story shared by the user.
        published_on (DateTimeField): Timestamp when the story was published.
        status (IntegerField): The publication status of the story.
        Choices are:
        - 0: Pending
        - 1: Published
    """

    journal_entry = models.OneToOneField(
        JournalEntry,
        on_delete=models.CASCADE
        )
    content = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"Story: {self.content[:20]}. Published on {self.published_on}"
