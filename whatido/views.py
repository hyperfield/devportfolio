from django.shortcuts import render

from .models import TaskCategory, Task


def whatido_index(request):
    categories = TaskCategory.objects.prefetch_related("tasks").all()
    context = {
        "task_categories": categories,
    }

    return render(request, "whatido_index.html", context)
