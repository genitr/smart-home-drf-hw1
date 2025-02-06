"""
URL configuration for smart_home project.
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('measurement.urls', namespace='measurement')),
]
