from django.db import models
from django.contrib.auth.models import User
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Task(models.Model):
    reporter = models.ForeignKey(User, related_name='reported_tasks', on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)
    labels = models.CharField(max_length=100)
    due_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(choices=[(tag.value, tag.name) for tag in Priority])
    description = models.TextField()
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)
