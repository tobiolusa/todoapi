from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
            'List' : '/task-list/',
            'Detail View' : '/task-detail/<str:pk>/',
            'Create' : 'task-create/',
            'Update' : '/task-update/<str:pk>/',
            'Delete' : '/task-delete/<str:pk>/',
        }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id = pk)
    tasks.delete()
    return Response("Task Deleted Successfully")
    