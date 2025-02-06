from django.contrib import admin

from .models import Measurement, Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    ordering = ('name', 'description')


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'created_at')
    search_fields = ('temperature', 'created_at')
    list_filter = ('temperature', 'created_at')
    ordering = ('temperature', 'created_at')
