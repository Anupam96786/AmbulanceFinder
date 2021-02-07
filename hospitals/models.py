from django.contrib.gis.db import models


class Hospital(models.Model):
    amenity = models.CharField(max_length=10, default='hospital')
    hid = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    location = models.PointField()
    address = models.TextField(blank=True, null=True)
    district = models.TextField(blank=True, null=True)
    postcode = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
