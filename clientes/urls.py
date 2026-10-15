"""Rutas del módulo Clientes. Todas quedan bajo /clientes/ (ya configurado)."""
from django.urls import path

from . import views

app_name = "clientes"

urlpatterns = [
    path("",           views.inicio,     name="inicio"),
    path("gestionar/", views.gestionar,  name="gestionar"),
]