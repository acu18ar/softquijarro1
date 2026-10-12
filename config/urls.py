"""
Rutas principales. ⚠️ ARCHIVO DEL DOCENTE: los estudiantes no lo modifican.

Cada módulo ya tiene su prefijo. Tus rutas nuevas van en TU archivo
<tu_app>/urls.py, nunca aquí.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ingresar/", auth_views.LoginView.as_view(), name="login"),
    path("salir/", auth_views.LogoutView.as_view(), name="logout"),
    path("clientes/", include("clientes.urls")),
    path("productos/", include("productos.urls")),
    path("facturacion/", include("facturacion.urls")),
    path("proveedores/", include("proveedores.urls")),
    path("reportes/", include("reportes.urls")),
    path("", include("core.urls")),
]

admin.site.site_header = "SoftQuijarro S.R.L. — Administración"
admin.site.site_title = "SoftQuijarro"
admin.site.index_title = "Panel de administración"
