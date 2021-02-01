from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.serializers import serialize
from .models import Hospital
import json
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance


@api_view(['POST'])
def get_hospitals(request):
    longitude = float(request.data['long'])
    latitude = float(request.data['lat'])
    user_location = Point(longitude, latitude, srid=4326)
    hospitals = serialize('geojson', queryset = Hospital.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:6])
    return Response(data={'data': json.loads(hospitals)})
