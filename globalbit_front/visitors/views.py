from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
from config import path


def home(request):

    return render(request, 'navbar.html')


def register(request):
    if request.method == 'POST':

        document = int(request.POST['document'])
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        data = {
            'document': document,
            'name': name,
            'phone_number': phone_number,
            'email': email
        }
        response = requests.post(
            path.get('BACKEND_ENDPOINT'), data=json.dumps(data))
        if response.status_code == 400:
            return redirect('user_exist')
        return redirect('register_success')
    return render(request, 'register_form.html')


def list_visitors(request):
    response = requests.get(path.get('BACKEND_ENDPOINT'))
    return render(request, 'visitors_list.html', {'users': response.json()})


def user_exist(request):
    return render(request, 'user_exist.html')


def register_success(request):
    return render(request, 'register_success.html')
