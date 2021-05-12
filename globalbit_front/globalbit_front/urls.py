from django.contrib import admin
from django.urls import path
from visitors import views as vs

urlpatterns = [
    path('', vs.home),
    path('register', vs.register, name='register'),
    path('list_visitors', vs.list_visitors),
    path('user_exist', vs.user_exist, name='user_exist'),
    path('register_success', vs.register_success, name='register_success')
]
