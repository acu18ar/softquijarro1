"""Pruebas del módulo Proveedores. Corre:  python manage.py test proveedores"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Proveedor


class ProveedoresTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user("prueba", password="x")
        self.client.force_login(usuario)

    def test_la_lista_muestra_los_proveedores(self):
        Proveedor.objects.create(nombre="Proveedor de prueba")
        respuesta = self.client.get(reverse("proveedores:inicio"))
        self.assertContains(respuesta, "Proveedor de prueba")

    # Agrega tus pruebas aquí.
