from django.db import models


class Proveedor(models.Model):
    TIPOS = [
        ("empresa", "Empresa"),
        ("persona", "Persona natural"),
    ]
    CATEGORIAS = [
        ("construccion", "Construcción"),
        ("herramientas", "Herramientas"),
        ("electricidad", "Electricidad"),
        ("plomeria", "Plomería"),
        ("pinturas", "Pinturas"),
        ("fijaciones", "Fijaciones y seguridad"),
        ("otra", "Otra"),
    ]

    # ── CAMPOS BASE ─────────────────────────────────────────────────────────
    nombre = models.CharField("nombre o razón social", max_length=150)
    telefono = models.CharField("teléfono o celular", max_length=30, blank=True)

    # ── A. Datos generales ──────────────────────────────────────────────────
    nit = models.CharField("NIT o CI", max_length=20, blank=True)
    tipo = models.CharField("tipo de proveedor", max_length=10, choices=TIPOS, default="empresa")
    categoria = models.CharField("categoría principal", max_length=20, choices=CATEGORIAS, default="otra")
    logo_url = models.URLField("logo (enlace a la imagen)", max_length=500, blank=True)

    # ── B. Información de contacto ──────────────────────────────────────────
    contacto = models.CharField("nombre del contacto", max_length=100, blank=True)
    correo = models.EmailField("correo electrónico", blank=True)
    direccion = models.CharField("dirección", max_length=200, blank=True)

    # ── C. Productos que surte (relación con Productos) ─────────────────────
    productos = models.ManyToManyField(
        "productos.Producto", blank=True, related_name="proveedores",
        verbose_name="productos que surte",
    )

    class Meta:
        ordering = ["nombre"]
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"

    @property
    def inicial(self):
        """Letra para el círculo que se muestra cuando no hay logo."""
        return self.nombre[:1].upper() if self.nombre else "?"

    def __str__(self):
        return self.nombre
