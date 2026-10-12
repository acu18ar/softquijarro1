"""Rutas del módulo Clientes. Todas quedan bajo /clientes/ (ya configurado)."""
from django.urls import path

from . import views

app_name = "clientes"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    # Agrega aquí tus rutas, por ejemplo:
    # path("nuevo/", views.nuevo, name="nuevo"),
]
