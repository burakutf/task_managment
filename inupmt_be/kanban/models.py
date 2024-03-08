from django.db import models

class Task(models.Model):
    reporter = models.CharField(max_length=100)
    dual_assignee = models.CharField(max_length=100)
    labels = models.CharField(max_length=100)
    due_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField()
    description = models.TextField()
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)
