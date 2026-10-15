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

    def test_crear_producto_valido(self):
        respuesta = self.client.post(reverse("productos:crear"), {
            "nombre": "Taladro",
            "categoria": "Herramientas",
            "proveedor": "Herramientas Industriales del Oriente",
            "precio": "250.00",
            "stock": 5,
            "stock_minimo": 2,
            "descripcion": "",
        })
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(Producto.objects.filter(nombre="Taladro").exists())

    def test_no_crea_producto_sin_nombre(self):
        respuesta = self.client.post(reverse("productos:crear"), {
            "nombre": "",
            "categoria": "Construcción",
            "precio": "10.00",
            "stock": 1,
            "stock_minimo": 1,
        })
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Producto.objects.count(), 0)

    def test_editar_producto(self):
        p = Producto.objects.create(nombre="Viejo", precio=10, stock=1)
        respuesta = self.client.post(reverse("productos:editar", args=[p.pk]), {
            "nombre": "Nuevo",
            "categoria": "Construcción",
            "proveedor": "",
            "precio": "20.00",
            "stock": 3,
            "stock_minimo": 1,
            "descripcion": "",
        })
        self.assertEqual(respuesta.status_code, 302)
        p.refresh_from_db()
        self.assertEqual(p.nombre, "Nuevo")

    def test_eliminar_producto(self):
        p = Producto.objects.create(nombre="Borrar", precio=10, stock=1)
        respuesta = self.client.post(reverse("productos:eliminar", args=[p.pk]))
        self.assertEqual(respuesta.status_code, 302)
        self.assertFalse(Producto.objects.filter(pk=p.pk).exists())

    def test_aviso_stock_bajo(self):
        Producto.objects.create(nombre="Escaso", precio=10, stock=1, stock_minimo=5)
        respuesta = self.client.get(reverse("productos:inicio"))
        self.assertContains(respuesta, "stock bajo")