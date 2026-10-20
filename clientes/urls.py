"""Rutas del módulo Clientes. Todas quedan bajo /clientes/ (ya configurado)."""
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from . import views

app_name = "clientes"

urlpatterns = [
    path("",           views.inicio,    name="inicio"),
    path("gestionar/", views.gestionar, name="gestionar"),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(
            r'^photos/(?P<path>.*)$',
            serve,
            {'document_root': settings.BASE_DIR / 'clientes' / 'Photos'},
        ),
    ]