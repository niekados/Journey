from django.shortcuts import render
from .models import HomeContent


def home_view(request):
    """
    Render the home page with the introduction and instructions content.
    """
    # Retrieve the first HomeContent object from the database
    home_content = HomeContent.objects.first()

    # Check if home_content exists
    if home_content is None:
        # Provide default content if no HomeContent is available
        home_content = {
            "introduction": "Introduction content not available.",
            "instructions": "Instructions content not available.",
        }

    return render(request, "home/index.html", {"home_content": home_content})
