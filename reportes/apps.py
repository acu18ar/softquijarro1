from django.apps import AppConfig


class ReportesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reportes"
    verbose_name = "Reportes"

    # ── Datos para el menú y el tablero. Estos SÍ los cambias tú ──────────
<<<<<<< HEAD
    responsable = "Sin asignar"          # ← escribe tu nombre
    estado = "en construcción"           # ← cámbialo a "listo" al terminar
=======
    responsable = "alberto"          # ← escribe tu nombre
    estado = "listo"           # ← cámbialo a "listo" al terminar
>>>>>>> 75a95613f60bda2004e352862a02c5fddd9b8c31
    icono = "bi-bar-chart-line"
    descripcion = "Ventas del día, productos más vendidos y clientes frecuentes."
    url_inicio = "reportes:inicio"
