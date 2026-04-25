from django.shortcuts import render , get_object_or_404
from .models import Project, Contact

def home(request):
    projects = Project.objects.all()
    return render(request, 'core/home.html', {'projects': projects})


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'core/project_detail.html', {'project': project})


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, 'core/contact.html', {'success': True})

    return render(request, 'core/contact.html')