"""Datos de prueba de Clientes. Si agregas campos obligatorios, complétalos aquí."""
from .models import Cliente

CLIENTES = [
    ("Constructora Pantanal Ltda.", "1023456027"),
    ("Juan Carlos Mamani", "6543210"),
    ("María Elena Rojas", "4891234"),
    ("Taller El Tornillo", "3021547015"),
    ("Hotel Frontera", "2034567019"),
    ("Ana Lucía Vargas", "7812345"),
    ("Agroindustrias Quijarro S.A.", "1029384021"),
    ("Pedro Gutiérrez Suárez", "5567890"),
]


def cargar():
    nuevos = 0
    for nombre, nit in CLIENTES:
        _, creado = Cliente.objects.get_or_create(nit=nit, defaults={"nombre": nombre})
        nuevos += creado
    return f"{nuevos} clientes nuevos ({Cliente.objects.count()} en total)"
