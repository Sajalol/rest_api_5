from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters, generics
from .serializers import TaskSerializer
from .models import Task
from django_api.permissions import IsOwnerOrReadOnly


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

    tasks = Task.objects.all()
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

"""
This Function going to display Detailed view of one perticuler task with the help of pk.
"""
@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many = False)
    return Response(serializer.data)

"Update single post"

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id = pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"Creating new posts"

@api_view(['POST'])
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