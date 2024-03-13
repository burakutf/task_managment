from django.db import models

from account.models import User


class Priority(models.TextChoices):
    LOW = 'low', 'Düşük'
    MEDIUM = 'medium', 'Orta'
    HIGH = 'high', 'Yüksek'


class Column(models.Model):
    title = models.CharField(max_length=100)
    priority = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class Labels(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.title}'


class Task(models.Model):
    reporter = models.ForeignKey(
        User,
        related_name='reported_tasks',
        on_delete=models.CASCADE,
    )
    assignees = models.ManyToManyField(User, related_name='assigned_tasks')
    column = models.ForeignKey(
        Column, related_name='tasks', on_delete=models.CASCADE, null=True
    )
    name = models.CharField(null=True, max_length=128)
    labels = models.ManyToManyField(Labels, related_name='labels_task')
    comments = models.ManyToManyField(User, related_name='comments_task')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    priority = models.TextField(choices=Priority.choices)
    description = models.TextField(null=True, blank=True)
    attachments = models.FileField(
        upload_to='attachments/', blank=True, null=True
    )

    def __str__(self):
        return f'{self.reporter} - {self.labels}'


class Comment(models.Model):
    task = models.ForeignKey(
        Task, related_name='task_comments', on_delete=models.CASCADE, null=True
    )

    author = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE, null=True
    )
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.task}'
