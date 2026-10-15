from django.db import models


class Producto(models.Model):
    # ── CAMPOS BASE (NO TOCAR) ──────────────────────────────────────────
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField("precio (Bs)", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    # ── CAMPOS NUEVOS ───────────────────────────────────────────────────
    CATEGORIA_CHOICES = [
        ("Construcción", "Construcción"),
        ("Herramientas", "Herramientas"),
        ("Electricidad", "Electricidad"),
        ("Plomería", "Plomería"),
        ("Pinturas", "Pinturas"),
        ("Fijaciones y seguridad", "Fijaciones y seguridad"),
    ]

    categoria = models.CharField(
        "categoría",
        max_length=50,
        choices=CATEGORIA_CHOICES,
        default="Construcción",
    )
    proveedor = models.CharField(
        "proveedor",
        max_length=150,
        blank=True,
        default="",
        help_text="Opcional. Se llenará cuando el módulo de Proveedores esté listo.",
    )
    descripcion = models.TextField(
        "descripción",
        blank=True,
        default="",
        help_text="Detalle opcional del producto.",
    )
    stock_minimo = models.PositiveIntegerField(
        "stock mínimo",
        default=5,
        help_text="Si el stock baja de este valor, se muestra alerta.",
    )

    class Meta:
        ordering = ["nombre"]
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre

    # ── PROPIEDADES ÚTILES ──────────────────────────────────────────────
    @property
    def stock_bajo(self):
        """True si el stock está por debajo o igual al mínimo."""
        return self.stock <= self.stock_minimo