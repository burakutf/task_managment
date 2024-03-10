from django.db import models

from account.models import User


class Priority(models.IntegerChoices):
    LOW = 1, 'Düşük'
    MEDIUM = 2, 'Orta'
    HIGH = 3, 'Yüksek'


class Column(models.Model):
    title = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title


class Comment(models.Model):

    author = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE
    )
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.task}'


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
    labels = models.CharField(max_length=100)
    due_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(choices=Priority.choices)
    description = models.TextField()
    attachments = models.FileField(
        upload_to='attachments/', blank=True, null=True
    )

    def __str__(self):
        return f'{self.reporter} - {self.labels}'
