from django.shortcuts import render

from item.models import Project

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {
        'projects': projects,
    })