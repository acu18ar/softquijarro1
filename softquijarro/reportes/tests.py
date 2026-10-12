"""Pruebas del módulo Reportes. Corre:  python manage.py test reportes"""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class ReportesTests(TestCase):
    def setUp(self):
        usuario = get_user_model().objects.create_user("prueba", password="x")
        self.client.force_login(usuario)

    def test_la_pagina_abre_sin_ventas(self):
        respuesta = self.client.get(reverse("reportes:inicio"))
        self.assertEqual(respuesta.status_code, 200)

    # Agrega tus pruebas aquí.
