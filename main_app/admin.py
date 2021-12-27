from django.contrib import admin
from .models import Car, Location, Sighting
# Register your models here.
admin.site.register(Car)
admin.site.register(Sighting)
admin.site.register(Location)