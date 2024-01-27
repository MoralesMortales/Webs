from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('HELLO WORLD')

def about(request):
    return HttpResponse('<h1>ABOUT</h1>')
# Create your views here.
