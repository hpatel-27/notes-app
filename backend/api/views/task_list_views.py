from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# from rest_framework.permissions import IsAuthenticated

from ..models import TaskList
from ..serializers import TaskListSerializer


# Get all the task lists for a user, Create a new task list
class TaskListListCreateView(APIView):
    """
    get:
        Return all the task lists for the user.

    post:
        Create a new task list with the given information.
    """

    def get(self, request):
        lists = TaskList.objects.all()
        serializer = TaskListSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data.copy()
        data["owner"] = request.user.id
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get a specific task list, update a specific task list, and delete a task list
class TaskListDetailView(APIView):
    def get(self, request, task_list_id):
        try:
            task_list = TaskList.objects.get(owner=request.user, id=task_list_id)
            serializer = TaskListSerializer(task_list)
            return Response(serializer.data)
        except TaskList.DoesNotExist:
            return Response(
                {"error": "Task list does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, task_list_id):
        try:
            task_list = TaskList.objects.get(owner=request.user, id=task_list_id)
            serializer = TaskListSerializer(task_list, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except TaskList.DoesNotExist:
            return Response(
                {"error": "Task list does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self, request, task_list_id):
        try:
            task_list = TaskList.objects.get(owner=request.user, id=task_list_id)
            task_list.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TaskList.DoesNotExist:
            return Response(
                {"error": "Task list does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )
