from django.shortcuts import render
from flights.models import Flight

def start(request):
    return render(request, 'start.html')

def about_drom(request):
    return render(request, 'about_drom.html')

def about_cost(request):
    return render(request, 'about_cost.html')
