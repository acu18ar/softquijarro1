from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("crear/", views.crear_producto, name="crear"),
    path("<int:pk>/editar/", views.editar_producto, name="editar"),
    path("<int:pk>/eliminar/", views.eliminar_producto, name="eliminar"),
]