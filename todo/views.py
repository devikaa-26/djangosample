from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):

    tasks = Task.objects.filter(user=request.user)

    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_task(request):

    title = request.data.get('title')

    task = Task.objects.create(
        user=request.user,
        title=title,
        completed=False
    )

    serializer = TaskSerializer(task)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, pk):

    task = Task.objects.get(id=pk, user=request.user)

    task.delete()

    return Response({"message": "Task Deleted"})