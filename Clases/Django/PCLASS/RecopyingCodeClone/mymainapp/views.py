from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ShowMainPage(TemplateView):
    template_name = 'index.html'
    

class ShowViewPage(TemplateView):
    template_name = "about.html"
