from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Task

def home(request):

    if request.method == "POST":
        title = request.POST["title"]
        due = request.POST["due"]
        task = Task(title = title, due_time = due)
        task.save()
        return redirect("/")

    name = "vedant"
    context = {
        "name": name.capitalize(),
        "tasks": Task.objects.filter(completed = False),
        "completed": Task.objects.filter(completed = True)
    }
    return render(request, "home.html", context)