from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

# class ShowMainPage(TemplateView):
#     template_name = 'index.html'
    

# class ShowViewPage(TemplateView):
#     template_name = "about.html"
    

    
class HomePageView(ListView):
    model= Post  
    template_name="home.html"

class AboutPageView(TemplateView):
    template_name="about.html"

class BlogDetailView(DetailView):
    model=Post
    template_name="post_detail.html"

class BlogCreateView(CreateView):
    model=Post
    template_name="post_new.html"
    fields= ["title", "author", "body"]
    success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
    model=Post
    template_name="post_edit.html"
    fields=["title", "body"]
    success_url = reverse_lazy('home')
    

class BlogDeleteView(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url= reverse_lazy("home")

