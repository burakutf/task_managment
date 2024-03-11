# Generated by Django 4.2.7 on 2024-03-11 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Labels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='labels',
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(related_name='labels_task', to='kanban.labels'),
        ),
    ]