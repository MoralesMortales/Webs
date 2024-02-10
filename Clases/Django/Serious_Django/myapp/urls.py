from django.urls import path
from .views import hello, about, index, sum, projects, tasks

urlpatterns = [
    path("", index, name=""),
    path("about/", about, name=""),
    path("projects/", projects),
    path("tasks/<int:id>", tasks),
    path("sum/<int:id>", sum, name=""),
    path("hello/<str:username>", hello, name=""),
]
