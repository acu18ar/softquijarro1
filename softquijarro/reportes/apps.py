from django.apps import AppConfig


class ReportesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reportes"
    verbose_name = "Reportes"

    # ── Datos para el menú y el tablero. Estos SÍ los cambias tú ──────────
    responsable = "Sin asignar"          # ← escribe tu nombre
    estado = "en construcción"           # ← cámbialo a "listo" al terminar
    icono = "bi-bar-chart-line"
    descripcion = "Ventas del día, productos más vendidos y clientes frecuentes."
    url_inicio = "reportes:inicio"
