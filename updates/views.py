from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Count

from .models import Update, Comment
from .forms import CommentForm


def updates_index(request):
    updates = Update.objects.all().order_by('-created_on')\
        .annotate(count=Count('comments'))
    context = {
        "updates": updates,
    }
    print("Comments: ", updates.count())

    return render(request, "updates_index.html", context)


def update_detail(request, pk):
    update = Update.objects.get(pk=pk)
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["comment"],
                update=update,
            )
            try:
                new_comment.save()
            except ValidationError:
                return HttpResponse('Could not submit the form.')
            try:
                from_email = 'inbox@quicknode.net'
                to_emails = [from_email]
                email_message = f"{new_comment.author}, {new_comment.body}"
                send_mail("New comment", email_message,
                          from_email, to_emails)
            except BadHeaderError:
                pass

    comments = Comment.objects.filter(update=update).order_by('-created_on')
    context = {
        "update": update,
        "comments": comments,
        "form": form,
    }

    return render(request, "update_detail.html", context)
