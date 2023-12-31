from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, UpdateView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context = {
            'posts': posts
        }
        return render(request, 'bloglist.html', context)
    
    
    
class PostDetailView(View):
    def get(self,request,pk ,*args, **kwargs): #PK PK PK PK PK PK PK PK PK PK PK PK PK P K PK PK PK PK PK 
        post = get_object_or_404(Post, pk = pk)
        context = {
            'post':post
        }
        return render(request,'blog_detail.html',context)


class BlogCreateView(View):
    def get(self,request,*args, **kwargs):
        form = PostCreateForm()
        context = {
            'form':form
            
        }
        
        return render(request, 'blog_create.html', context)
    
    def post(self,request,*args, **kwargs):
        
        if request.method=="POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                description = form.cleaned_data.get('description')
                p, created = Post.objects.get_or_create(title = title, description = description)
                p.save()
                return redirect('blog:homee')
                
        context = {
        
        }
        
        return render(request, 'blog_create.html', context)

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'description']
    template_name = "blog_update.html"
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs = {'pk':pk})