from django.contrib import admin
from django.urls import path, include
from . import locations

urlpatterns = [
    path('', include(locations.urls)),
]
