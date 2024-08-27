from django.db import models
from djrichtextfield.models import RichTextField


class HomeContent(models.Model):
    """
    Represents the content displayed on the home page of the Journey app.

    Attributes:
        introduction (RichTextField): Introduction for the home page.
        instructions (RichTextField): Instructions to guide users on
        how to use the Journey app.
        created_on (DateTimeField): The timestamp of when the content was last
            updated or created.
    """

    introduction = RichTextField(null=False, blank=False)
    instructions = RichTextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Home content updated on {self.created_on}"
