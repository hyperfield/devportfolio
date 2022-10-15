from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from adminsortable2.admin import SortableAdminMixin

from .models import TaskCategory, Task


@admin.register(TaskCategory)
class TaskCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class TaskCategoryInline(SortableInlineAdminMixin, admin.TabularInline):
    model = TaskCategory


@admin.register(Task)
class TaskAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass


class TaskInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Task
