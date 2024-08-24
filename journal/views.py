from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_journal(request):
    return HttpResponse("This is My Journal app and it is working!")