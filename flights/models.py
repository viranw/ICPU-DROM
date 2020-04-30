from django.db import models

# Create your models here.

ff_tiers = [
    ['bronze','QF Bronze'],
    ['qf_club', 'QF Club'],
    ['silver','QF Silver'],
    ['gold','QF Gold'],
    ['platinum','QF Platinum'],
    ['platinum_one','QF Platinum One'],
    ['cl','QF Chairmans'],

    ['ek_silver','EK Skywards Silver'],
    ['ek_gold','EK Skywards Gold'],
    ['ek_platinum','EK Skywards Platinum'],

    ['ow_ruby','Oneworld Ruby'],
    ['ow_sapphire','Oneworld Sapphire'],
    ['ow_emerald','Oneworld Emerald']

]

class Flight(models.Model):
    name = models.CharField(max_length=50, verbose_name="Flight Identifier", help_text="The flight number, or other name to title this flight.")
    date = models.DateField()

    def __str__(self):
        return "[{}] {}".format(self.date_code(), self.name)

    def passengers_by_name(self):
        return self.passenger_set.all().order_by('name')

    def date_code(self):
        return self.date.strftime("%Y%m%d")

class Passenger(models.Model):
    name = models.CharField(max_length=200)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    ff = models.CharField(max_length=50, choices=ff_tiers, verbose_name="FF Status", null=True, blank=True)
    url_key = models.SlugField(null=True, blank=True, unique=True, verbose_name="URL Key", help_text="The unique identifier that is used to create the passenger's unique page.")

    def __str__(self):
        return "[{} {}] {}".format(self.flight.date_code(), self.flight.name, self.name)
