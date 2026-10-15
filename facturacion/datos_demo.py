"""Ventas de prueba, para que Reportes tenga datos desde el primer día.

Solo se cargan si todavía no hay ninguna factura. No descuentan stock.
"""
import random
from datetime import timedelta

from django.utils import timezone

from clientes.models import Cliente
from productos.models import Producto

from .models import DetalleFactura, Factura


def cargar():
    if Factura.objects.exists():
        return f"ya hay {Factura.objects.count()} facturas, no se agregan más"
    clientes = list(Cliente.objects.all())
    productos = list(Producto.objects.all())
    if not clientes or not productos:
        return "sin clientes o productos, no se generan facturas"

    azar = random.Random(2026)  # siempre los mismos datos
    ahora = timezone.now()
    fechas = sorted(
        ahora - timedelta(days=azar.randint(0, 13), hours=azar.randint(0, 9))
        for _ in range(15)
    )
    for fecha in fechas:  # en orden, para que el N.º de factura siga a la fecha
        factura = Factura.objects.create(cliente=azar.choice(clientes), fecha=fecha)
        total = 0
        for producto in azar.sample(productos, azar.randint(1, 3)):
            linea = DetalleFactura.objects.create(
                factura=factura,
                producto=producto,
                cantidad=azar.randint(1, 10),
                precio_unitario=producto.precio,
            )
            total += linea.subtotal
        factura.total = total
        factura.save(update_fields=["total"])
    return f"{Factura.objects.count()} facturas de prueba"
