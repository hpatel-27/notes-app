from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TaskList(models.Model):
    """
    A TaskList groups the ListItems (to-do tasks) for a user.
    The ListItem will keep the foreign key of the associated TaskList.

    Each task list has:
    - title: Title of the list
    - owner: The user that owns this task list
    - created_at: The date that the task list was created
    - updated_at: The date and time that the task list was last updated
    """

    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_lists")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
