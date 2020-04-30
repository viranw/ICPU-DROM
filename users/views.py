from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse
from urllib.parse import urlencode

# Commented out until the custom login is implemented

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            username = request.POST['username']
            auth.login(request, user)

            return redirect('start')
        else:
            return render(request, 'users/login.html', {'error': 'The username or password is incorrect.'})

    return render(request, 'users/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('start')

    return render(request, 'start.html')
