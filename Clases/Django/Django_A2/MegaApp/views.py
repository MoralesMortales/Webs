from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

def printHello(request):
    return HttpResponse("Prueba de impresion")

class HomePage(TemplateView):
    template_name = "home.html"

class AboutPage(TemplateView):
    template_name = "about.html"
    
class ContactPage(TemplateView):
    template_name = "contact.html"
