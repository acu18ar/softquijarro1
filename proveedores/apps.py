from django.apps import AppConfig


class ProveedoresConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "proveedores"
    verbose_name = "Proveedores"

    # ── Datos para el menú y el tablero. Estos SÍ los cambias tú ──────────
    responsable = "Sin asignar"          # ← escribe tu nombre
    estado = "en construcción"           # ← cámbialo a "listo" al terminar
    icono = "bi-truck"
    descripcion = "Proveedores de la ferretería y qué productos surten."
    url_inicio = "proveedores:inicio"
