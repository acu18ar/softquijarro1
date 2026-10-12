"""Rutas del módulo Reportes. Todas quedan bajo /reportes/ (ya configurado)."""
from django.urls import path

from . import views

app_name = "reportes"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    # Agrega aquí tus rutas, por ejemplo:
    # path("mas-vendidos/", views.mas_vendidos, name="mas_vendidos"),
]
