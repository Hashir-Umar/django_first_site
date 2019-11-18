from django.http import HttpResponse

# from quotes.models import


def index(request):
    return HttpResponse("hello")
