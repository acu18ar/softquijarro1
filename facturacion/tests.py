"""Pruebas del módulo Facturación. Corre:  python manage.py test facturacion"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from clientes.models import Cliente

from .models import Factura


class FacturacionTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user("prueba", password="x")
        self.client.force_login(usuario)

    def test_la_lista_muestra_las_facturas(self):
        cliente = Cliente.objects.create(nombre="Cliente Factura", nit="999")
        Factura.objects.create(cliente=cliente, total=100)
        respuesta = self.client.get(reverse("facturacion:inicio"))
        self.assertContains(respuesta, "Cliente Factura")

    # Agrega tus pruebas aquí. Ejemplo para la historia del stock:
    # def test_facturar_descuenta_stock(self): ...
