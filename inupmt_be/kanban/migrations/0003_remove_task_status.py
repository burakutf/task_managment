# Generated by Django 4.2.7 on 2024-03-10 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0002_column_task_status_task_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
