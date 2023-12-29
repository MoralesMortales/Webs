from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

def printsm(request):
    return HttpResponse("Prueba de impresion")


class MyIndex(TemplateView):
    template_name = "Index.html"


class MyInfo(TemplateView):
    template_name = "Information.html"
