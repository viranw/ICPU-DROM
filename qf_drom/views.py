from django.shortcuts import render
from flights.models import Flight

def start(request):
    return render(request, 'start.html')
