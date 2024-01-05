from django.contrib import admin
from .views import ShowMainPage, ShowCreateListPage, ShowListPage
from django.urls import path


app_name = 'app1'

urlpatterns = [
    path("", ShowMainPage.as_view(), name="Main"),
    path("CreateList/", ShowCreateListPage.as_view(), name="CreateList"),
    path("ListPage/", ShowListPage.as_view(), name="ListPage")
]

