# Generated by Django 4.2.7 on 2024-03-11 19:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kanban', '0007_rename_finish_date_task_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comments',
            field=models.ManyToManyField(related_name='comments_task', to=settings.AUTH_USER_MODEL),
        ),
    ]
