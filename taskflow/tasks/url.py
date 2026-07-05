from django.urls import path
from . import views

urlpatterns = [path('', views.home), 
               path("task-complete/<int:id>/",views.completeTask), 
               path("delete-task/<int:id>/",views.deleteTask),
               path("get-tasks/", views.addTasks),]