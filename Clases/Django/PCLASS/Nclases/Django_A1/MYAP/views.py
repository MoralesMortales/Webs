from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def PrintHello(request):
    return HttpResponse("Hello There!")

class HomePageView(TemplateView):
    template_name = "myap/home.html"
    

class AboutPageView(TemplateView):
    template_name = "myap/about.html"
    
