from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.objects.all()
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
