from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def home(request):
    name = "vedant"
    context = {
        "name": name.capitalize(),
        "tasks": Task.objects.filter(completed = False),
        "completed": Task.objects.filter(completed = True)
    }
    return render(request, "home.html", context)