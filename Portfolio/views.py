from django.shortcuts import render
from projects.models import Project


def index(request):
    projects = Project.objects.filter(published='1').order_by('priority')  # query db
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)


