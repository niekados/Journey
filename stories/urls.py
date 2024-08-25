from django.urls import path
from .views import Stories


urlpatterns = [
    path('', Stories.as_view(), name='stories',)
]
