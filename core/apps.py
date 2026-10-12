from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Base común: login, menú, plantilla base y datos de demo. Es del docente."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    verbose_name = "Base común"


# Orden en que aparecen los módulos en el menú y en que se cargan los datos
# de prueba (clientes y productos primero, porque facturación los usa).
MODULOS = ["clientes", "productos", "proveedores", "facturacion", "reportes"]
