"""
python manage.py asegurar_admin

Crea el usuario administrador si todavía no existe.
  - En Codespaces / tu PC: usuario "admin", contraseña "admin123".
  - En Render: usa las variables ADMIN_USUARIO y ADMIN_CLAVE que el docente
    definió al crear el servicio. Si no están, no crea nada.
"""
import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Crea el superusuario si no existe (idempotente)."

    def handle(self, *args, **options):
        if settings.DEBUG:
            usuario = os.environ.get("ADMIN_USUARIO", "admin")
            clave = os.environ.get("ADMIN_CLAVE", "admin123")
        else:
            usuario = os.environ.get("ADMIN_USUARIO")
            clave = os.environ.get("ADMIN_CLAVE")
            if not (usuario and clave):
                self.stdout.write("ADMIN_USUARIO / ADMIN_CLAVE no definidos: no se crea admin.")
                return

        User = get_user_model()
        if User.objects.filter(username=usuario).exists():
            self.stdout.write(f"El usuario '{usuario}' ya existe.")
            return
        User.objects.create_superuser(username=usuario, password=clave, email="")
        self.stdout.write(self.style.SUCCESS(f"Usuario administrador '{usuario}' creado."))
