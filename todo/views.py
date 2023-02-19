from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, generics
from .serializers import TaskSerializer
from .models import Task
from django_api.permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import get_object_or_404


"""
API Overview
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<int:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<int:pk>/',
        'Delete' : '/task-delete/<int:pk>/',
    }
    return Response(api_urls)

"Get tasklist and create a search filter "

class TaskList(generics.ListAPIView):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'due_date',
        'assigned_to',
        'category',
        'priority',
        'completed',
    ]
    search_fields = [
        'title',
    ]
    ordering_fields = [
        'due_date',
        'assigned_to',
        'category',
        'priority',
        'completed',
    ]

    def perform_create(self, serializer):
        return Response(serializer.data)
        
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TaskCreateSerializer
        else:
            return TaskSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.method == 'POST':
            context.update({"user": self.request.user})
        return context

"""
This Function going to display Detailed view of one perticuler task with the help of pk.
"""
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)

"Update single post"

@api_view(['PUT', 'PATCH', 'GET'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)

    serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    if serializer.is_valid():
        completed_subtasks = 0
        total_subtasks = task.subtasks.count()

        for subtask in task.subtasks.all():
            if subtask.completed:
                completed_subtasks += 1

        if total_subtasks == 0:
            task.completed_percentage = 0
        else:
            task.completed_percentage = int((completed_subtasks / total_subtasks) * 100)

        serializer.save()

    return Response(serializer.data)


"Creating new posts"

@api_view(['GET', 'POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"Delete posts"

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return Response("Task deleted successfully.")

"Show all users"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'last_name', 'email']


@api_view(['GET'])
def all_users(request):
    users = User.objects.all()
    serialized_users = UserSerializer(users, many=True)
    return Response(serialized_users.data)



"User detailed view"

@api_view(['GET'])
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)