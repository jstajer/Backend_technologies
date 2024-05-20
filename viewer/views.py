from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello World!")

def hello2(request, s):
    return HttpResponse(f'Hello {s} World !')

def hello3(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello {s} World ! World!')

