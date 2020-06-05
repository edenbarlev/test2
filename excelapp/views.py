import csv

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render


# Create your views here.



def about(request):
    return HttpResponse('<h1>Blog About hello hello</h1>')


def loading(request):
    template = 'excelapp/loader.html'
    return render(request, template)

def uploading(request):
    template = 'excelapp/loadData.html'
    return render(request, template)

def contact(request):
    return HttpResponse('contant view')

def index(request):
    template = 'excelapp/loader.html'
    return render(request, template)
