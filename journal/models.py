from django.db import models
from django.apps import apps
from django.contrib.auth.models import User


class JournalEntry(models.Model):
    """
    Represents a journal entry made by a user. Each entry can be
    marked as public or private.

    Attributes:
        user (ForeignKey): The user who created the journal entry.
        mood (CharField): User's mood from the predefined choices.
        day_description (CharField): A brief description of the day.
        content (TextField): The main content of the journal entry.
        grateful_for (TextField): Reflect on what the user is grateful for.
        improve_on (TextField): Reflect on what user wants to improve.
        created_on (DateTimeField): Creation timestamp.
        is_public (BooleanField): Indicates if entry is public.
    """

    MOOD_CHOICES = [
        ("happy", "Happy"),
        ("normal", "Normal"),
        ("sad", "Sad"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="journal_author"
    )
    mood = models.CharField(
        max_length=10,
        choices=MOOD_CHOICES,
        default="normal"
        )
    day_description = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField()
    grateful_for = models.TextField(blank=True)
    improve_on = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.day_description} by {self.user.username}"

    def publish_as_story(self):
        """Publish the journal entry as a story if it is marked public."""
        if self.is_public:
            StoryEntry = apps.get_model("stories", "StoryEntry")
            story_entry, created = StoryEntry.objects.get_or_create(
                journal_entry=self,
                defaults={"content": self.content},
            )
            if not created and story_entry.content != self.content:
                # Update the content if it has changed
                story_entry.content = self.content
                story_entry.save()

    def unpublish_story(self):
        """Unpublish the journal entry from the community stories."""
        if not self.is_public:
            StoryEntry = apps.get_model("stories", "StoryEntry")
            StoryEntry.objects.filter(journal_entry=self).delete()
