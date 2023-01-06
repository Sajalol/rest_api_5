from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.apiOverview, name="Todo-list"),
    path('todo/task-list/', views.taskList, name="task-list")
  ]