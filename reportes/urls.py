<<<<<<< HEAD
"""Rutas del módulo Reportes. Todas quedan bajo /reportes/ (ya configurado)."""
=======
"""Rutas del módulo Reportes. Todas quedan bajo /reportes/."""
>>>>>>> 75a95613f60bda2004e352862a02c5fddd9b8c31
from django.urls import path

from . import views

app_name = "reportes"

urlpatterns = [
    path("", views.inicio, name="inicio"),
<<<<<<< HEAD
    # Agrega aquí tus rutas, por ejemplo:
    # path("mas-vendidos/", views.mas_vendidos, name="mas_vendidos"),
]
=======
    path("imprimir/", views.reporte_imprimible, name="imprimir"),
]
>>>>>>> 75a95613f60bda2004e352862a02c5fddd9b8c31
