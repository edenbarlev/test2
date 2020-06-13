import csv

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render


# Create your views here.
from .forms import DocumentForm


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

def form(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES.get('document')
            #form.save()
            return render(request, 'excelapp/loader.html', myfile)
    else:
        form = DocumentForm()
    return render(request, 'excelapp/loadexcelform.html', {
        'form': form
    })

