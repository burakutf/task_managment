# Generated by Django 4.2.7 on 2024-03-11 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0010_alter_comment_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='order',
            new_name='priority',
        ),
    ]
