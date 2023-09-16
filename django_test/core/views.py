from django.shortcuts import render
from django.views.generic.edit import FormView
from django.core.mail import EmailMessage

from item.models import Project
from .forms import MessageForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

# def contact(request):
#     return render(request, 'core/contact.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'core/projects.html', {
        'projects': projects,
    })

class MessageView(FormView):
    template_name = 'core/contact.html'
    form_class = MessageForm
    success_url = ''

    def form_valid(self, form):
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        email_subject = 'Contact Message'
        email_body = f"Email: {email}\nMessage: {message}"
        email_sender = 'ryan_pereda83@gmail.com'
        email_recepient = 'ryan_pereda83@gmail.com'

        email_message = EmailMessage(
            email_subject,
            email_body,
            email_sender,
            [email_recepient],
        )
        email_message.send()

        return super().form_valid(form)