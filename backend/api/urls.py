from .views import TaskListDetailView, TaskListListCreateView
from django.urls import path

urlpatterns = [
    path("tasks/", TaskListListCreateView.as_view(), name="tasks_list"),
    path(
        "tasks/<int:task_list_id>",
        TaskListDetailView.as_view(),
        name="task_lists_details",
    ),
]
