"""Rutas del módulo Reportes. Todas quedan bajo /reportes/."""
from django.urls import path

from . import views

app_name = "reportes"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("imprimir/", views.reporte_imprimible, name="imprimir"),
]