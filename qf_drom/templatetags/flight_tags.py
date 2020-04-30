from django import template
from flights.models import Flight

register = template.Library()

@register.simple_tag
def all_flights():
    return Flight.objects.all()
