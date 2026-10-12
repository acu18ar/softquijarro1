import os

from django.apps import apps
from django.urls import NoReverseMatch, reverse

from .apps import MODULOS


def _modulos():
    """Arma el menú leyendo el apps.py de cada módulo.

    Cada estudiante cambia SU apps.py (responsable, icono, estado) y el menú
    se actualiza solo, sin que nadie toque la plantilla base.
    """
    modulos = []
    for nombre in MODULOS:
        cfg = apps.get_app_config(nombre)
        try:
            url = reverse(getattr(cfg, "url_inicio", f"{nombre}:inicio"))
        except NoReverseMatch:
            url = None
        modulos.append(
            {
                "app": nombre,
                "nombre": cfg.verbose_name,
                "icono": getattr(cfg, "icono", "bi-box"),
                "descripcion": getattr(cfg, "descripcion", ""),
                "responsable": getattr(cfg, "responsable", "Sin asignar"),
                "estado": getattr(cfg, "estado", "en construcción"),
                "url": url,
            }
        )
    return modulos


def menu_modulos(request):
    commit = os.environ.get("RENDER_GIT_COMMIT", "")
    return {
        "modulos_menu": _modulos(),
        "version_desplegada": commit[:7] if commit else "desarrollo",
    }
