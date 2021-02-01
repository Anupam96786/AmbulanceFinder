from django.shortcuts import render
from django.http.response import HttpResponse
from hospitals.models import Hospital
from django.contrib.gis.geos import Point
import time


def index(request):
    return render(request, 'home.html')


