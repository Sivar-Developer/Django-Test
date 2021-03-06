from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus', views.aboutus, name="aboutus"),
    path('single/<slug:slug>', views.single, name="single"),
]
