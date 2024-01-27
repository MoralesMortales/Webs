from django.urls import path
from .views import hello, about

urlpatterns = [
    path("", hello, name=""),
    path("about/", about, name=""),
]
