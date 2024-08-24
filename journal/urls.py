from django.urls import path
from .views import Journal

urlpatterns = [
    path("", Journal.as_view(), name="journal"),
]
