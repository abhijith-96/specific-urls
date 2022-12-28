from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def second(request):
    return HttpResponse('<marquee>this is my second specific url</marquee>')
