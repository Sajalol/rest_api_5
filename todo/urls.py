from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.apiOverview, name="Todo-list"),
    path('todo/task-list/', views.taskList, name="task-list"),
    path('todo/task-detail/<int:pk>/', views.taskDetail, name="task-Detail"),
    path('todo/task-update/<int:pk>/', views.taskUpdate, name="task-update"),
    path('todo/task-create/', views.taskCreate, name="Task-Create"),
    path('todo/task-delete/<int:pk>/', views.taskDelete, name="task-delete"),
  ]