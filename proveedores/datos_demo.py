"""Datos de prueba de Proveedores. Si agregas campos obligatorios, complétalos aquí."""
from .models import Proveedor

PROVEEDORES = [
    ("Distribuidora Santa Cruz Ferretera", "3-3456789"),
    ("Aceros del Oriente S.R.L.", "3-3512233"),
    ("Pinturas Corumbá (Brasil)", "+55 67 3231-0000"),
    ("Importadora Eléctrica Chiquitana", "7-1234567"),
]


def cargar():
    nuevos = 0
    for nombre, telefono in PROVEEDORES:
        _, creado = Proveedor.objects.get_or_create(nombre=nombre, defaults={"telefono": telefono})
        nuevos += creado
    return f"{nuevos} proveedores nuevos ({Proveedor.objects.count()} en total)"
