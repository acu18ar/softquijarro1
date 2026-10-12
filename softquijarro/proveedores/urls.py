"""Rutas del módulo Proveedores. Todas quedan bajo /proveedores/ (ya configurado)."""
from django.urls import path

from . import views

app_name = "proveedores"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    # Agrega aquí tus rutas.
]
