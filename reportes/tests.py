"""Pruebas del módulo Reportes. Corre:  python manage.py test reportes"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

<<<<<<< HEAD
=======
from productos.models import Producto

>>>>>>> 75a95613f60bda2004e352862a02c5fddd9b8c31

class ReportesTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user("prueba", password="x")
        self.client.force_login(usuario)

<<<<<<< HEAD
    def test_la_pagina_abre_sin_ventas(self):
        respuesta = self.client.get(reverse("reportes:inicio"))
        self.assertEqual(respuesta.status_code, 200)

    # Agrega tus pruebas aquí.
=======
    def test_la_pagina_abre_sin_datos(self):
        respuesta = self.client.get(reverse("reportes:inicio"))
        self.assertEqual(respuesta.status_code, 200)

    def test_muestra_productos_con_stock_bajo(self):
        Producto.objects.create(
            nombre="Clavo oxidado",
            precio=10,
            stock=1,
            stock_minimo=5,
            categoria="Construcción",
        )
        respuesta = self.client.get(reverse("reportes:inicio"))
        self.assertContains(respuesta, "Clavo oxidado")

    def test_muestra_conteo_productos(self):
        Producto.objects.create(nombre="A", precio=1, stock=10, categoria="Construcción")
        Producto.objects.create(nombre="B", precio=2, stock=5, categoria="Electricidad")
        respuesta = self.client.get(reverse("reportes:inicio"))
        self.assertEqual(respuesta.context["total_productos"], 2)
>>>>>>> 75a95613f60bda2004e352862a02c5fddd9b8c31
