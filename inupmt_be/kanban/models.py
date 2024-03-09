from django.db import models
from django.contrib.auth.models import User as AuthUser

class Priority(models.IntegerChoices):
    LOW = 1, 'Düşük'
    MEDIUM = 2, 'Orta'
    HIGH = 3, 'Yüksek'

class Task(models.Model):
    reporter = models.ForeignKey(AuthUser, related_name='reported_tasks', on_delete=models.CASCADE)
    assignees = models.ManyToManyField(AuthUser, related_name='assigned_tasks')
    labels = models.CharField(max_length=100)
    due_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(choices=Priority.choices)    
    description = models.TextField()
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)

class UserModel(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)