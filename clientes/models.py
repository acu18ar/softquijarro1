from django.db import models


class Cliente(models.Model):
    # ── CAMPOS BASE ─────────────────────────────────────────────────────────
    # Facturación y Reportes usan estos campos. NO los borres ni les cambies
    # el nombre: romperías el trabajo de tus compañeros (y la verificación
    # automática de GitHub lo va a detectar).
    nombre = models.CharField("nombre o razón social", max_length=150)
    nit = models.CharField("NIT / CI", max_length=20)

    # ── TUS CAMPOS NUEVOS VAN AQUÍ ──────────────────────────────────────────
    # Regla: todo campo nuevo lleva blank=True, null=True o un default,
    # para que los datos que ya existen no se rompan.
    # Ejemplo:  telefono = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "cliente"
        verbose_name_plural = "clientes"

    def __str__(self):
        return f"{self.nombre} ({self.nit})"
