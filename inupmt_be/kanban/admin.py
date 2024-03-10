from django.contrib import admin

from kanban.models import Column, Task

# Register your models here.

admin.site.register(Task)
admin.site.register(Column)
