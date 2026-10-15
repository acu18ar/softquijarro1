"""Rutas del módulo Proveedores. Todas quedan bajo /proveedores/ (ya configurado)."""
from django.urls import path

from . import views

app_name = "proveedores"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nuevo/", views.crear, name="crear"),
    path("<int:pk>/", views.detalle, name="detalle"),
    path("<int:pk>/editar/", views.editar, name="editar"),
    path("<int:pk>/eliminar/", views.eliminar, name="eliminar"),
]
