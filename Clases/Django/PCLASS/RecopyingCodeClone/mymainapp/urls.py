from .views import ShowMainPage, ShowViewPage
from django.urls import path

urlpatterns = [
    path("", ShowMainPage.as_view(), name="index"),
    path("about/", ShowViewPage.as_view(), name="about"),
]

