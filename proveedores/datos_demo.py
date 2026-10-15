"""Datos de prueba de Proveedores. Si agregas campos obligatorios, complétalos aquí.

Los datos son ficticios (NIT, celulares y correos @example.com).
Los productos se asignan por palabra clave del nombre; Productos se carga antes
que Proveedores, así que ya existen cuando corre esto.
"""
from productos.models import Producto

from .models import Proveedor

# nombre, telefono, nit, tipo, categoria, contacto, correo, direccion, palabras de productos
PROVEEDORES = [
    ("Distribuidora Santa Cruz Ferretera", "3-3456789", "", "empresa", "otra", "", "", "",
     ["Cemento", "Clavos", "Martillo", "Llave"]),
    ("Aceros del Oriente S.R.L.", "3-3512233", "", "empresa", "construccion", "", "", "",
     ["Fierro", "Calamina"]),
    ("Pinturas Corumbá (Brasil)", "+55 67 3231-0000", "", "empresa", "pinturas", "", "", "",
     ["Pintura"]),
    ("Importadora Eléctrica Chiquitana", "7-1234567", "", "empresa", "electricidad", "", "", "",
     ["Cable", "Foco"]),
    ("Materiales de Construcción El Constructor", "70000001", "4587216018", "empresa",
     "construccion", "Juan Carlos Méndez Rojas", "constructor.ejemplo@example.com",
     "Av. Principal N.º 120, Zona Central, Puerto Suárez, Santa Cruz, Bolivia",
     ["Cemento", "Fierro", "Calamina"]),
    ("Herramientas Industriales del Oriente", "70000002", "4587216026", "empresa",
     "herramientas", "Roberto Salvatierra Flores", "herramientas.ejemplo@example.com",
     "Calle Comercio N.º 45, Zona Comercial, Puerto Suárez, Santa Cruz, Bolivia",
     ["Martillo", "Llave"]),
    ("Distribuidora Eléctrica Central", "70000003", "4587216034", "empresa",
     "electricidad", "María Fernanda Suárez Lima", "electrica.ejemplo@example.com",
     "Av. Bolívar N.º 88, Zona Central, Puerto Suárez, Santa Cruz, Bolivia",
     ["Cable", "Foco"]),
    ("Hidráulica y Plomería San José", "70000004", "4587216042", "empresa",
     "plomeria", "Miguel Ángel Vargas Ortiz", "plomeria.ejemplo@example.com",
     "Calle Sucre N.º 67, Zona Norte, Puerto Suárez, Santa Cruz, Bolivia",
     ["Tubo"]),
    ("Pinturas y Acabados ColorMax", "70000005", "4587216050", "empresa",
     "pinturas", "Andrea Paola Chávez Roca", "pinturas.ejemplo@example.com",
     "Av. Santa Cruz N.º 105, Zona Comercial, Puerto Suárez, Santa Cruz, Bolivia",
     ["Pintura"]),
    ("Tornillos y Accesorios La Llave", "70000006", "4587216069", "empresa",
     "fijaciones", "Óscar Daniel Rojas Méndez", "accesorios.ejemplo@example.com",
     "Calle 6 de Agosto N.º 32, Zona Central, Puerto Suárez, Santa Cruz, Bolivia",
     ["Clavos"]),
]


def cargar():
    nuevos = 0
    for (nombre, telefono, nit, tipo, categoria, contacto, correo, direccion,
         palabras) in PROVEEDORES:
        proveedor, creado = Proveedor.objects.get_or_create(
            nombre=nombre,
            defaults={
                "telefono": telefono, "nit": nit, "tipo": tipo, "categoria": categoria,
                "contacto": contacto, "correo": correo, "direccion": direccion,
            },
        )
        nuevos += creado
        for palabra in palabras:
            proveedor.productos.add(*Producto.objects.filter(nombre__icontains=palabra))
    return f"{nuevos} proveedores nuevos ({Proveedor.objects.count()} en total)"
