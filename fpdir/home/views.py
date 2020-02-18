from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    context = {

    }
    return render(request, 'home/home.html', context)
