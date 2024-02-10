from .views import AboutPageView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView, CreateView, DeleteView, DetailView, HomePageView, ListView
from django.urls import path

urlpatterns=[
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("post/<int:pk>", BlogDetailView.as_view(), name='post_detail'),
    path("post/new", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name='post_edit'),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name='post_delete'),
]
