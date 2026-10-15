from django.apps import AppConfig


class ProveedoresConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "proveedores"
    verbose_name = "Proveedores"

   
    responsable = "Kevin Surubi"          
    estado = "listo"          
    icono = "bi-truck"
    descripcion = "Proveedores de la ferretería y qué productos surten."
    url_inicio = "proveedores:inicio"
