from django.contrib import admin

from .models import TaskCategory, Task


@admin.register(TaskCategory)
class TaskCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
