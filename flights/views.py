from django.shortcuts import render
from django.http import Http404
from flights.models import *

from django.contrib.auth.decorators import user_passes_test


def sample_flight_home(request, flight_id):
    params = {}

    try:
        flight = Flight.objects.get(pk=flight_id)
        params['flight'] = flight
    except Exception:
        raise Http404

    return render(request, 'flights/flight_home.html', params)

def sample_flight_passengers(request, flight_id):
    params = {}

    try:
        flight = Flight.objects.get(pk=flight_id)
        params['flight'] = flight
    except Exception:
        raise Http404

    return render(request, 'flights/sample_passengers.html', params)

def sample_flight_reaccom(request, flight_id):
    params = {}

    try:
        flight = Flight.objects.get(pk=flight_id)
        params['flight'] = flight
    except Exception:
        raise Http404

    return render(request, 'flights/sample_reaccom.html', params)

# Create your views here.
@user_passes_test(lambda u: u.is_superuser)
def flight_dashboard(request, flight_id):
    params = {}

    try:
        flight = Flight.objects.get(pk=flight_id)
        params['flight'] = flight
    except Exception:
        raise Http404

    return render(request, 'flights/admin/dashboard.html', params)

@user_passes_test(lambda u: u.is_superuser)
def passengers(request, flight_id):
    params = {}

    try:
        flight = Flight.objects.get(pk=flight_id)
        params['flight'] = flight
    except Exception:
        raise Http404

    return render(request, 'flights/admin/passengers.html', params)

@user_passes_test(lambda u: u.is_superuser)
def reaccom(request, flight_id):
    params = {}

    try:
        flight = Flight.objects.get(pk=flight_id)
        params['flight'] = flight
    except Exception:
        raise Http404

    return render(request, 'flights/admin/reaccom.html', params)

def passenger_page(request, url_key):
    params = {}

    try:
        passenger = Passenger.objects.get(url_key=url_key)
        params['passenger'] = passenger
    except Exception:
        raise Http404

    return render(request, 'flights/passenger.html', params)
