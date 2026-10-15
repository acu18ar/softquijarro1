"""
python manage.py cargar_datos_demo

Llama a la función cargar() del archivo datos_demo.py de cada módulo.
Se puede correr las veces que quieras: no duplica datos.

Cada estudiante es dueño del datos_demo.py de SU módulo. Si agregas un
campo obligatorio a tu modelo, actualiza tu datos_demo.py en el mismo
pull request; si no, la verificación automática falla.
"""
from importlib import import_module

from django.core.management.base import BaseCommand
from django.db import transaction

from core.apps import MODULOS


class Command(BaseCommand):
    help = "Carga los datos de prueba de todos los módulos (sin duplicar)."

    def handle(self, *args, **options):
        for nombre in MODULOS:
            try:
                modulo = import_module(f"{nombre}.datos_demo")
            except ModuleNotFoundError:
                self.stdout.write(f"  · {nombre}: sin datos de prueba")
                continue
            with transaction.atomic():
                resultado = modulo.cargar()
            self.stdout.write(self.style.SUCCESS(f"  ✓ {nombre}: {resultado}"))
        self.stdout.write(self.style.SUCCESS("Datos de prueba listos."))
