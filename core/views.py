from django.shortcuts import render , get_object_or_404
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'core/home.html', {'projects': projects})


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'core/project_detail.html', {'project': project})