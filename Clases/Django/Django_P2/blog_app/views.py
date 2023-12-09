from django.views.generic import TemplateView

class homepageview(TemplateView):
    template_name="home.html"


class aboutpageview(TemplateView):
    template_name="about.html"
# Create your views here.

