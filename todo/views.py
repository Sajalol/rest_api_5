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
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.db.models import Q
import logging

logger = logging.getLogger(__name__)


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.created_by == request.user


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

    def get_queryset(self):
        assigned_to = self.request.GET.get('assigned_to')
        search = self.request.GET.get('search')
        priority_filter = self.request.GET.get('priority_filter')
        category_filter = self.request.GET.get('category_filter')
        sort_field = self.request.GET.get('sort_field')
        sort_order = self.request.GET.get('sort_order')

        queryset = Task.objects.filter(assigned_to=assigned_to)

        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(content__icontains=search))

        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)

        if category_filter:
            queryset = queryset.filter(category=category_filter)

        if sort_field and sort_order:
            sort_prefix = '' if sort_order == 'asc' else '-'
            queryset = queryset.order_by(f'{sort_prefix}{sort_field}')

        return queryset

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
@permission_classes([IsAuthenticated, IsOwnerOrReadOnly])
def taskUpdate(request, pk):
    logger.info("Incoming request data: %s", request.data)
    
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()

        logger.info("Response data: %s", serializer.data)
        return Response(serializer.data)
    else:
        logger.error("Invalid request data: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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