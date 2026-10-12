"""Pruebas del módulo Clientes. Corre:  python manage.py test clientes"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Cliente


class ClientesTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user("prueba", password="x")
        self.client.force_login(usuario)

    def test_la_lista_muestra_los_clientes(self):
        Cliente.objects.create(nombre="Cliente de prueba", nit="123")
        respuesta = self.client.get(reverse("clientes:inicio"))
        self.assertContains(respuesta, "Cliente de prueba")

    # Agrega tus pruebas aquí. Ejemplo para la historia del NIT repetido:
    # def test_no_permite_nit_repetido(self): ...
