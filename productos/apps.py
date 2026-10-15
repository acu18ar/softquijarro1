from django.apps import AppConfig


class ProductosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "productos"
    verbose_name = "Productos"

    # ── Datos para el menú y el tablero. Estos SÍ los cambias tú ──────────
    responsable = "Sin asignar"          # ← escribe tu nombre
    estado = "listo"           # ← cámbialo a "listo" al terminar
    icono = "bi-box-seam"
    descripcion = "Catálogo de la ferretería con precio y stock."
    url_inicio = "productos:inicio"
