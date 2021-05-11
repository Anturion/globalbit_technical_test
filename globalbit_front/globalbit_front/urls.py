from django.contrib import admin
from django.urls import path
from visitors import views as vs

urlpatterns = [
    path('', vs.home),
    path('register', vs.register),
    path('list_visitors', vs.list_visitors)
]
