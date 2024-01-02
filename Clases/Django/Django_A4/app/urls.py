from django.urls import path, include
from .views import BlogListView

app_name = 'app'

urlpatterns = [
    path('',BlogListView.as_view(), name='homee')
]
