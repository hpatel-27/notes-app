from rest_framework import serializers
from .models import ListItem, TaskList


class ListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItem
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    items = ListItemSerializer(many=True, read_only=True)

    class Meta:
        model = TaskList
        fields = "__all__"
