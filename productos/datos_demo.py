"""Datos de prueba de Productos. Si agregas campos obligatorios, complétalos aquí."""
from decimal import Decimal

from .models import Producto

PRODUCTOS = [
    # (nombre, precio, stock, categoría, proveedor)
    ("Cemento Viacha 50 kg", "62.00", 120, "Construcción", "Materiales de Construcción El Constructor"),
    ('Fierro corrugado 3/8" (barra 12 m)', "48.50", 300, "Construcción", "Materiales de Construcción El Constructor"),
    ('Clavos de 2" (kg)', "18.00", 80, "Construcción", "Materiales de Construcción El Constructor"),
    ("Pintura látex blanca 4 L", "135.00", 25, "Pinturas", "Pinturas y Acabados ColorMax"),
    ("Martillo de carpintero", "55.00", 15, "Herramientas", "Herramientas Industriales del Oriente"),
    ('Tubo PVC 1/2" (6 m)', "22.00", 60, "Plomería", "Hidráulica y Plomería San José"),
    ("Cable eléctrico N.º 12 (rollo 100 m)", "390.00", 8, "Electricidad", "Distribuidora Eléctrica Central"),
    ('Llave inglesa 10"', "75.00", 4, "Herramientas", "Herramientas Industriales del Oriente"),
    ("Calamina galvanizada 3 m", "68.00", 150, "Construcción", "Materiales de Construcción El Constructor"),
    ("Foco LED 12 W", "15.00", 200, "Electricidad", "Distribuidora Eléctrica Central"),
]


def cargar():
    nuevos = 0
    for nombre, precio, stock, categoria, proveedor in PRODUCTOS:
        _, creado = Producto.objects.get_or_create(
            nombre=nombre,
            defaults={
                "precio": Decimal(precio),
                "stock": stock,
                "categoria": categoria,
                "proveedor": proveedor,
            },
        )
        nuevos += creado
    return f"{nuevos} productos nuevos ({Producto.objects.count()} en total)"