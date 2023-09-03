from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def projects(request):
    return render(request, 'core/projects.html')