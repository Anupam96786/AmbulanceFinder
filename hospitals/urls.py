from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_hospitals, name='get_nearby_hospitals'),
]