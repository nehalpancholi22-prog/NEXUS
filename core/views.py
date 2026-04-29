from django.shortcuts import render , get_object_or_404
from .models import Project, Contact
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    projects = Project.objects.all()
    return render(request, 'core/home.html', {'projects': projects})


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'core/project_detail.html', {'project': project})

def edit_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.tech_stack = request.POST.get('tech_stack')
        project.github_link = request.POST.get('github_link')
        project.live_demo = request.POST.get('live_demo')

        project.save()
        return redirect('project_detail', id=project.id)

    return render(request, 'core/edit_project.html', {'project': project})

def delete_project(request, id):
    project = get_object_or_404(Project, id=id)

    if request.method == 'POST':
        project.delete()
        return redirect('home')

    return render(request, 'core/delete_confirm.html', {'project': project})

@login_required
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



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Invalid credentials'})

    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('/')