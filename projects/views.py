from django.shortcuts import render
from projects.models import Project


def project_index(request):
    projects = Project.objects.filter(published='1').order_by('priority')  # query db
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)  # query db
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)