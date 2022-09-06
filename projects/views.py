from django.shortcuts import render
from projects.models import Project


def project_index(request, category=None, technology=None):
    if not category and not technology:
        projects = Project.objects.all()
    elif category:
        projects = Project.objects.filter(category__title=category)
    else:
        projects = Project.objects.filter(
            technologies__title=technology
            )
    context = {
        'projects': projects,
    }

    return render(request, 'project_index.html', context)


def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    context = {
      'project': project,
      'project_images': project.gallery.all(),
    }

    return render(request, 'project_detail.html', context)
