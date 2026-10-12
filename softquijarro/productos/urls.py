"""Rutas del módulo Productos. Todas quedan bajo /productos/ (ya configurado)."""
from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    # Agrega aquí tus rutas.
]
