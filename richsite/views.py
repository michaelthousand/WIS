from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.contrib import messages

from django.template.loader import render_to_string


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'name': 'Name: ' + form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name'],
                'email': 'Email: ' + form.cleaned_data['email_address'],
                'phone_number': 'Phone number: ' + form.cleaned_data['phone_number'],
                'subject': 'Subject: ' + form.cleaned_data['subject'],
                'message': 'Message: ' + form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            messages.success(request, 'Thanks for submitting!', extra_tags='success')

            html = render_to_string('contactform.html', {
                'name': form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'phone_number': form.cleaned_data['phone_number'],
                'subject': form.cleaned_data['subject'],
                'message': form.cleaned_data['message'],
            })

            try:
                send_mail(subject, message, 'rich@williamsinvestigations.org', ['rich@williamsinvestigations.org'], html_message=html)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("contact")
        
    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'form': form
    })

def contactsuccess(request):
    return render(request, 'contact.html')


