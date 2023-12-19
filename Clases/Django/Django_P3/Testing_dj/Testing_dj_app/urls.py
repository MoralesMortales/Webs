from django.urls import path
from .views import homePageViewmifuncion

urlpatterns = [
    path("", homePageViewmifuncion, name="home")
]