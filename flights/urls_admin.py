from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.flight_dashboard, name="flight_dashboard"),
    path('passengers',views.passengers, name="passengers"),

]
