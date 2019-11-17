from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from quotes.models import Quote


def index(request):
    list_of_recent_posted__quote = Quote.objects.order_by('-posted_date')[:6]
    template = loader.get_template('quotes/index.html')
    context = {
        'list_of_recent_posted__quote': list_of_recent_posted__quote,
    }
    return render(request, 'quotes/index.html', context)


def detail(request, quote_id):
    return HttpResponse("You are looking for quote %s" % quote_id)


def result(request, quote_id):
    return HttpResponse("You are looking for the result of quote %s" % quote_id)
