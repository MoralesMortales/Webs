from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs): #Se coloca por default/ self se aplica para llamarse a si mismo a una def en py
        context = {
            
        }
        
        return render(request,'index.html', context) #request pide al servidor, lo otro es la dirreccion, y el context el contenido adicional a utilizar