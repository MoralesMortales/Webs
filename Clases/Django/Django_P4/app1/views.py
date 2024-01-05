from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView
# Create your views here.


class ShowMainPage(TemplateView):
    template_name = "index.html"

class ShowCreateListPage(View):
    def get(self, request, *args, **kwargs):
     pass

class ShowListPage(TemplateView):
    template_name = "ListPage.html"
