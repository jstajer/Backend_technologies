from django.http import HttpResponse
from django.shortcuts import render

from viewer.models import *


def hello(request):
    return HttpResponse("Hello World!")

def hello2(request, s):
    return HttpResponse(f'Hello {s} World !')

def hello3(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello {s} World ! World!')

def hello4(request):
    adjectives = ['nice', 'cruel', 'beautiful', 'sunny']

    return render(
        request = request , #předáváme na další stránku request (obsahuje např. data o přihlášeném uživateli)

        template_name="hello.html" ,
        context={"adjectives": adjectives, 'name': 'Jirka' } )

def movies(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies.html', context)
