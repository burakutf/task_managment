# Generated by Django 4.2.7 on 2024-03-11 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0011_rename_order_column_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=128, null=True),
        ),
    ]