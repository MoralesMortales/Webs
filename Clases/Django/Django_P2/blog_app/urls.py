from django.urls import path
from .views import homepageview, aboutpageview

urlpatterns=[
    path("",  homepageview.as_view(), name="home"),
    path("about/", aboutpageview.as_view(), name="about" ) 

]