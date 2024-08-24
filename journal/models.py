from django.db import models
from django.contrib.auth.models import User


class JournalEntry(models.Model):
    MOOD_CHOICES = [
        ('happy', "Happy"),
        ('normal', "Normal"),
        ('sad', "Sad"),
    ]
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="journal_author"
    )
    mood = models.IntegerField(choices=MOOD_CHOICES, default="normal")
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
