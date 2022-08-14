from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_page(request, sent=False, filled_form=None):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            filled_form = form.cleaned_data
            try:
                send_mail(subject, message, from_email,
                          ['pzarva@quicknode.net'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return redirect('success')

    email = 'pzarva...quicknode...net'
    context = {
        'email': email,
        'form': form,
        'sent': sent,
        'filled_form': filled_form,
    }

    return render(request, 'contact_page.html', context)


# def email_success(request):
#     return contact_page(request, sent=True)
