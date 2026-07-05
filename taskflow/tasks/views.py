from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from .models import Task

def home(request):

    if request.method == "POST":
        title = request.POST["title"]
        due = request.POST["due"]
        due = due[:-6]+' @ '+due[-5:] if due else ""
        task = Task(title = title, due_time = due, completed = False)
        task.save()
        return redirect("/")

    name = "vedant"
    context = {
        "name": name.capitalize(),
    }
    return render(request, "home.html", context)

def completeTask(request, id):
    try:
        task = Task.objects.get(id = id)
        task.completed = True
        task.save()
        return JsonResponse({
            "id": id,
            "success": True,
        })
    except:
        return JsonResponse({
            "id": id,
            "success": False,
        })

def deleteTask(request, id):
    try:
        task = Task.objects.get(id = id)
        task.delete()
        return JsonResponse({
            "id": id,
            "success": True,
        })
    except:
        return JsonResponse({
            "id": id,
            "success": False,
        })
    
def addTasks(request):
    name = "vedant"
    tasks = list(
    Task.objects.filter(completed=False).values(
            "id",
            "title",
            "due_time"
        )
    )
    completed = list(
        Task.objects.filter(completed=True).values(
            "id",
            "title",
            "due_time"
        )
    )

    return JsonResponse({
        "tasks": tasks,
        "completed": completed
    })