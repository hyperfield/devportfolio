from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


def contact_page(request, sent=False, filled_form=None):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = 'inbox@quicknode.net'
            user_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            filled_form = form.cleaned_data

            email = EmailMessage(
                subject,
                message,
                from_email,
                ['inbox@quicknode.net'],
                reply_to=[user_email]
            )

            try:
                email.send()
                sent = True
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    email = 'pzarva...quicknode...net'
    context = {
        'email': email,
        'form': form,
        'sent': sent,
        'filled_form': filled_form,
    }

    return render(request, 'contact_page.html', context)
