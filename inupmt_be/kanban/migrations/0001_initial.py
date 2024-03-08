# Generated by Django 5.0.2 on 2024-03-08 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporter', models.CharField(max_length=100)),
                ('dual_assignee', models.CharField(max_length=100)),
                ('labels', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('priority', models.IntegerField()),
                ('description', models.TextField()),
                ('attachments', models.FileField(blank=True, null=True, upload_to='attachments/')),
            ],
        ),
    ]