from django.db import models


class Proveedor(models.Model):
    # ── CAMPOS BASE ─────────────────────────────────────────────────────────
    nombre = models.CharField("nombre o razón social", max_length=150)
    telefono = models.CharField("teléfono", max_length=30, blank=True)

    # ── TUS CAMPOS NUEVOS VAN AQUÍ ──────────────────────────────────────────
    # Regla: todo campo nuevo lleva blank=True, null=True o un default.
    # La relación con productos la defines TÚ, aquí, sin tocar el módulo
    # Productos. Pista:
    #   productos = models.ManyToManyField("productos.Producto", blank=True,
    #                                      related_name="proveedores")

    class Meta:
        ordering = ["nombre"]
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"

    def __str__(self):
        return self.nombre
