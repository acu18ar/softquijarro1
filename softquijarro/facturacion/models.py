from django.db import models
from django.utils import timezone


class Factura(models.Model):
    # ── CAMPOS BASE ─────────────────────────────────────────────────────────
    # Reportes usa estos campos. NO los borres ni les cambies el nombre.
    cliente = models.ForeignKey(
        "clientes.Cliente", on_delete=models.PROTECT, related_name="facturas"
    )
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField("total (Bs)", max_digits=12, decimal_places=2, default=0)

    # ── TUS CAMPOS NUEVOS VAN AQUÍ ──────────────────────────────────────────
    # Regla: todo campo nuevo lleva blank=True, null=True o un default.

    class Meta:
        ordering = ["-fecha"]
        verbose_name = "factura"
        verbose_name_plural = "facturas"

    def __str__(self):
        return f"Factura N.º {self.pk} — {self.cliente.nombre}"


class DetalleFactura(models.Model):
    # ── CAMPOS BASE ─────────────────────────────────────────────────────────
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(
        "productos.Producto", on_delete=models.PROTECT, related_name="ventas"
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "línea de factura"
        verbose_name_plural = "líneas de factura"

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} × {self.producto.nombre}"
