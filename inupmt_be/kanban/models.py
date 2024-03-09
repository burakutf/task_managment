from django.db import models
from django.contrib.auth.models import User
from enum import IntEnum

class Priority(models.IntegerChoices):
    LOW = 1, 'Düşük'
    MEDIUM = 2, 'Orta'
    HIGH = 3, 'Yüksek'

class Task(models.Model):
    reporter = models.ForeignKey(User, related_name='reported_tasks', on_delete=models.CASCADE)
    assignees = models.ManyToManyField(User, related_name='assigned_tasks')
    labels = models.CharField(max_length=100)
    due_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(choices=[(tag.value, tag.name) for tag in Priority])
    description = models.TextField()
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)
