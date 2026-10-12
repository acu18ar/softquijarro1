from django.db import models


class Producto(models.Model):
    # ── CAMPOS BASE ─────────────────────────────────────────────────────────
    # Facturación, Proveedores y Reportes usan estos campos.
    # NO los borres ni les cambies el nombre.
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField("precio (Bs)", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    # ── TUS CAMPOS NUEVOS VAN AQUÍ ──────────────────────────────────────────
    # Regla: todo campo nuevo lleva blank=True, null=True o un default.
    # Ejemplo:  stock_minimo = models.PositiveIntegerField(default=5)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre
