from django.contrib import admin

from kanban.models import Column, Labels, Task,Comment

# Register your models here.

admin.site.register(Task)
admin.site.register(Column)
admin.site.register(Labels)
admin.site.register(Comment)