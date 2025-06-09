from django.db import models
from task_list import TaskList


class ListItem(models.Model):
    """
    A ListItem contains information about the task to be completed.

    Each ListItems contains:
    - is_completed: A flag that indicates whether a task is complete.
    - description: The information about the task to complete.
    - due_date: The date that the task should be completed by.
    - priority: The level of priority that the task has (Low, Medium, High).
    """

    task_list = models.ForeignKey(
        TaskList, on_delete=models.CASCADE, related_name="items"
    )
    is_completed = models.BooleanField(default=False)
    description = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    updated_now = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
