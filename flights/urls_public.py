from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.sample_flight_home, name="sample_flight_home"),
    path('passengers',views.sample_flight_passengers, name="sample_flight_passengers"),
    path('reaccom',views.sample_flight_reaccom, name="sample_flight_reaccom"),


]
