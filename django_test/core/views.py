from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from item.models import Project
from .forms import MessageForm

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        print(f"apples {form.cleaned_data['email']}\nbananas {form.cleaned_data['message']}")
        
        if form.is_valid():
            send_mail(
                "Contact me email",
                f"{form['email']}\n{form['message']}",
                settings.EMAIL_HOST_USER,
                ["ryanpereda83@gmail.com"],
                fail_silently=False,
            )

            return redirect('core:contact')
        
    else:
        form = MessageForm()
    return render(request, 'core/contact.html', {
        'form': form
    })

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
        email_sender = 'ryanpereda83@gmail.com'
        email_recepient = 'ryanpereda83@gmail.com'

        email_message = EmailMessage(
            email_subject,
            email_body,
            email_sender,
            [email_recepient],
        )
        email_message.send()

        return super().form_valid(form)