from django.http import HttpResponse


def robots_view(request):
    with open('robots.txt', 'r') as file:
        text = file.read()
    return HttpResponse(text, content_type="text/plain")
