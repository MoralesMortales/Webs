from django.urls import path, include
from .views import BlogListView, BlogCreateView,PostDetailView,BlogUpdateView

app_name = 'app1'

urlpatterns = [
    path('estaseninicio/',BlogListView.as_view(), name='homee'),
    path('estasenpost/',BlogCreateView.as_view(), name='create'),
    path('<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('<int:pk>/update/',BlogUpdateView.as_view(),name='post-update')
]
