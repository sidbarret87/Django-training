from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Здесь будет выведен список объявлений")
# Create your views here.
