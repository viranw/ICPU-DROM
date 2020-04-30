from django.contrib import admin
from .models import *

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['name','date']
    list_filter = ['date']

    ordering = ['date', 'name']

    #inlines = [ScoreInline, NomInline]

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['name','flight']
    list_filter = ['flight']

    ordering = ['flight', 'name']
