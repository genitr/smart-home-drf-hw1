"""
URL configuration for measurement application.
"""
from django.urls import include, path

from . views import SensorListView, RetrieveSensor, MeasurementCreate


app_name = 'measurement'

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensors'),
    path('sensors/<pk>/', RetrieveSensor.as_view(), name='sensor'),
    path('measurements/', MeasurementCreate.as_view(), name='measurement'),
]
