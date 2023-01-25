from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Bb
def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bb.objects.all()
    context = {'bbs':bbs}
    return render (request, 'bboard/index.html',{'bbs':bbs})

# Create your views here.
