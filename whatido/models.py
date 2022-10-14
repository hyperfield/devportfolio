from django.db import models
from tinymce.models import HTMLField


class TaskCategory(models.Model):
    category_name = models.CharField(max_length=25)
    category_desc = HTMLField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Task Categories'

    def __str__(self):
        return self.category_name


class Task(models.Model):
    task_name = models.CharField(max_length=250)
    task_desc = HTMLField(blank=True, null=True)
    task_category = models.ForeignKey('TaskCategory', on_delete=models.CASCADE,
                                      null=True, blank=False,
                                      related_name='tasks')

    def __str__(self):
        return self.task_name
