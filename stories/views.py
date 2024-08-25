from django.views.generic import ListView
from .models import StoryEntry


class Stories(ListView):
    """
    Displays a list of published stories, ordered by the most recent
    publication date, with pagination.
    """
    model = StoryEntry
    queryset = StoryEntry.objects.filter(status=1).order_by('-published_on')
    template_name = "stories/stories.html"
    context_object_name = "stories_list"
    paginate_by = 3
