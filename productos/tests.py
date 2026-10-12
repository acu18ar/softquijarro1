"""Pruebas del módulo Productos. Corre:  python manage.py test productos"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Producto


class ProductosTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user("prueba", password="x")
        self.client.force_login(usuario)

    def test_la_lista_muestra_los_productos(self):
        Producto.objects.create(nombre="Serrucho", precio=40, stock=3)
        respuesta = self.client.get(reverse("productos:inicio"))
        self.assertContains(respuesta, "Serrucho")

    # Agrega tus pruebas aquí.
