from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    return render(request, 'navbar.html')


def register(request):

    return render(request, 'register_form.html')


def list_visitors(request):

    return HttpResponse('Hola Mundo')
