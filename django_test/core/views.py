from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http import FileResponse

from item.models import Project
from .forms import MessageForm
from .models import PDF

# Create your views here.

def index(request):
    pdf = PDF.objects.first()
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            send_mail(
                "Contact me email",
                f"{form.cleaned_data['email']}\n\n{form.cleaned_data['message']}",
                settings.EMAIL_HOST_USER,
                ["ryanpereda83@gmail.com"],
                fail_silently=False,
            )

            return redirect('core:index')
        
    else:
        form = MessageForm()
    return render(request, 'core/index.html', {
        'form': form,
        'pdf': pdf
    })

def pdf_view(request, pdf_id):
    pdf = get_object_or_404(PDF, pk=pdf_id)
    pdf_path = pdf.file.path
    response = FileResponse(open(pdf_path, 'rb'))
    return response

def projects(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {
        'projects': projects,
    })

# def contact(request):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)

#         if form.is_valid():
#             send_mail(
#                 "Contact me email",
#                 f"{form.cleaned_data['email']}\n\n{form.cleaned_data['message']}",
#                 settings.EMAIL_HOST_USER,
#                 ["ryanpereda83@gmail.com"],
#                 fail_silently=False,
#             )

#             return redirect('core:contact')
        
#     else:
#         form = MessageForm()
#     return render(request, 'core/contact.html', {
#         'form': form
#     })