from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Tasks

def index(request):
 return HttpResponse('Index Page')

def hello(request, username):
    print(username)
    return HttpResponse('HELLO %s' % username.upper())

def sum(request, id):
    print(id*100)
    result = id*3
    return HttpResponse('HELLO Your sum is 3 times id and that\'s %i' % result)

def about(request):
    return HttpResponse('<h1>ABOUT</h1>')

def projects(request):
    projects = list(Project.objects.values()) # se debe convertir a lista asi que usas list()
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = Tasks.objects.get(id = id)
    return HttpResponse('<h1>tasks is %s</h1>' %task.title)
# Create your views here.
