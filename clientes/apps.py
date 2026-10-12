from django.apps import AppConfig


class ClientesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "clientes"
    verbose_name = "Clientes"

    # ── Datos para el menú y el tablero. Estos SÍ los cambias tú ──────────
    responsable = "Sin asignar"          # ← escribe tu nombre
    estado = "en construcción"           # ← cámbialo a "listo" al terminar
    icono = "bi-people"                  # iconos: https://icons.getbootstrap.com
    descripcion = "Registro y búsqueda de clientes con NIT o CI."
    url_inicio = "clientes:inicio"
