from django.apps import AppConfig


class ProveedoresConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "proveedores"
    verbose_name = "Proveedores"

<<<<<<< HEAD
   
    responsable = "Kevin Surubi"          
    estado = "listo"          
=======
    # ── Datos para el menú y el tablero. Estos SÍ los cambias tú ──────────
    responsable = "Sin asignar"          # ← escribe tu nombre
    estado = "en construcción"           # ← cámbialo a "listo" al terminar
>>>>>>> 75a95613f60bda2004e352862a02c5fddd9b8c31
    icono = "bi-truck"
    descripcion = "Proveedores de la ferretería y qué productos surten."
    url_inicio = "proveedores:inicio"
