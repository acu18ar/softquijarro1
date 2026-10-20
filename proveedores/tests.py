"""Pruebas del módulo Proveedores. Corre:  python manage.py test proveedores"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from productos.models import Producto

from .models import Proveedor


class ProveedoresTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user("prueba", password="x")
        self.client.force_login(usuario)

    def datos(self, **extra):
        base = {
            "nombre": "Proveedor nuevo", "nit": "123456", "tipo": "empresa",
            "categoria": "herramientas", "contacto": "Ana Pérez", "telefono": "70000000",
            "correo": "ana@example.com", "direccion": "Calle 1",
        }
        base.update(extra)
        return base

    def test_la_lista_muestra_los_proveedores(self):
        Proveedor.objects.create(nombre="Proveedor de prueba")
        respuesta = self.client.get(reverse("proveedores:inicio"))
        self.assertContains(respuesta, "Proveedor de prueba")

    def test_buscar_por_nombre(self):
        Proveedor.objects.create(nombre="Aceros del Oriente")
        Proveedor.objects.create(nombre="Pinturas ColorMax")
        respuesta = self.client.get(reverse("proveedores:inicio"), {"q": "aceros"})
        self.assertContains(respuesta, "Aceros del Oriente")
        self.assertNotContains(respuesta, "Pinturas ColorMax")

    def test_filtrar_por_categoria(self):
        Proveedor.objects.create(nombre="Eléctrica Uno", categoria="electricidad")
        Proveedor.objects.create(nombre="Plomería Dos", categoria="plomeria")
        respuesta = self.client.get(reverse("proveedores:inicio"), {"categoria": "plomeria"})
        self.assertContains(respuesta, "Plomería Dos")
        self.assertNotContains(respuesta, "Eléctrica Uno")

    def test_registrar_proveedor(self):
        respuesta = self.client.post(reverse("proveedores:crear"), self.datos(), follow=True)
        self.assertContains(respuesta, "registrado")
        self.assertTrue(Proveedor.objects.filter(nombre="Proveedor nuevo").exists())

    def test_logo_se_muestra_si_existe_y_si_no_hay_inicial(self):
        Proveedor.objects.create(nombre="Con Logo", logo_url="https://example.com/logo.png")
        Proveedor.objects.create(nombre="Zeta Sin Logo")
        respuesta = self.client.get(reverse("proveedores:inicio"))
        self.assertContains(respuesta, "https://example.com/logo.png")
        self.assertContains(respuesta, ">Z</span>")

    def test_telefono_es_obligatorio_en_el_formulario(self):
        respuesta = self.client.post(reverse("proveedores:crear"), self.datos(telefono=""))
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(Proveedor.objects.filter(nombre="Proveedor nuevo").exists())

    def test_editar_proveedor(self):
        proveedor = Proveedor.objects.create(nombre="Viejo", telefono="1")
        respuesta = self.client.post(
            reverse("proveedores:editar", args=[proveedor.pk]), self.datos(nombre="Nuevo nombre"),
            follow=True,
        )
        self.assertContains(respuesta, "actualizado")
        proveedor.refresh_from_db()
        self.assertEqual(proveedor.nombre, "Nuevo nombre")

    def test_ficha_muestra_productos_y_stock(self):
        proveedor = Proveedor.objects.create(nombre="Surtidor")
        producto = Producto.objects.create(nombre="Cemento", precio=Decimal("62"), stock=77)
        proveedor.productos.add(producto)
        respuesta = self.client.get(reverse("proveedores:detalle", args=[proveedor.pk]))
        self.assertContains(respuesta, "Cemento")
        self.assertContains(respuesta, "77")

    def test_eliminar_proveedor(self):
        proveedor = Proveedor.objects.create(nombre="Borrar")
        self.client.post(reverse("proveedores:eliminar", args=[proveedor.pk]))
        self.assertFalse(Proveedor.objects.filter(pk=proveedor.pk).exists())
