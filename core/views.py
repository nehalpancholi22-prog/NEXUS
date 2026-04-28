from django.shortcuts import render , get_object_or_404
from .models import Project, Contact
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    projects = Project.objects.all()
    return render(request, 'core/home.html', {'projects': projects})


@login_required
def add_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        tech_stack = request.POST.get('tech_stack')
        github_link = request.POST.get('github_link')
        live_demo = request.POST.get('live_demo')

        Project.objects.create(
            title=title,
            description=description,
            tech_stack=tech_stack,
            github_link=github_link,
            live_demo=live_demo
        )

        return redirect('home')

    return render(request, 'core/add_project.html')




def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'core/project_detail.html', {'project': project})



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