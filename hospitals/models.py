from django.contrib.gis.db import models


class Hospital(models.Model):
    name = models.TextField(blank=False, null=False)
    location = models.PointField()
    landmark = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

