from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
class Priority(models.IntegerChoices):
    LOW = 1, 'Düşük'
    MEDIUM = 2, 'Orta'
    HIGH = 3, 'Yüksek'

class Task(models.Model):
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reported_tasks', on_delete=models.CASCADE)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='assigned_tasks')
    labels = models.CharField(max_length=100)
    due_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(choices=Priority.choices)    
    description = models.TextField()
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Kullanıcılar'
