from django.contrib.gis import admin
from .models import Hospital


@admin.register(Hospital)
class HospitalAdmin(admin.OSMGeoAdmin):
    list_display = ['name', 'location']
