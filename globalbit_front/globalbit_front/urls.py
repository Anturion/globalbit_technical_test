from django.contrib import admin
from django.urls import path
from visitors import views as vs

urlpatterns = [
    path('home/', vs.home),
]
