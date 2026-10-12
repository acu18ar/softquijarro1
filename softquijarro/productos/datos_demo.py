"""Datos de prueba de Productos. Si agregas campos obligatorios, complétalos aquí."""
from decimal import Decimal

from .models import Producto

PRODUCTOS = [
    ("Cemento Viacha 50 kg", "62.00", 120),
    ("Fierro corrugado 3/8\" (barra 12 m)", "48.50", 300),
    ("Clavos de 2\" (kg)", "18.00", 80),
    ("Pintura látex blanca 4 L", "135.00", 25),
    ("Martillo de carpintero", "55.00", 15),
    ("Tubo PVC 1/2\" (6 m)", "22.00", 60),
    ("Cable eléctrico N.º 12 (rollo 100 m)", "390.00", 8),
    ("Llave inglesa 10\"", "75.00", 4),
    ("Calamina galvanizada 3 m", "68.00", 150),
    ("Foco LED 12 W", "15.00", 200),
]


def cargar():
    nuevos = 0
    for nombre, precio, stock in PRODUCTOS:
        _, creado = Producto.objects.get_or_create(
            nombre=nombre, defaults={"precio": Decimal(precio), "stock": stock}
        )
        nuevos += creado
    return f"{nuevos} productos nuevos ({Producto.objects.count()} en total)"
