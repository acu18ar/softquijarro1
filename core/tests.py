"""
PRUEBAS DE CONTRATO (del docente). Corren en cada pull request.

Verifican que ningún cambio rompa lo que los otros módulos necesitan:
  - los CAMPOS BASE de cada modelo siguen existiendo,
  - los datos de prueba se cargan sin errores,
  - la página de inicio de cada módulo abre.
Si una de estas falla en tu pull request, NO es culpa del sistema:
tu cambio rompió algo que otro compañero usa. Revisa el mensaje.
"""
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from clientes.models import Cliente
from facturacion.models import DetalleFactura, Factura
from productos.models import Producto
from proveedores.models import Proveedor

CAMPOS_BASE = {
    Cliente: ["nombre", "nit"],
    Producto: ["nombre", "precio", "stock"],
    Proveedor: ["nombre", "telefono"],
    Factura: ["cliente", "fecha", "total"],
    DetalleFactura: ["factura", "producto", "cantidad", "precio_unitario"],
}


class ContratoEntreModulos(TestCase):
    def test_los_campos_base_siguen_existiendo(self):
        for modelo, campos in CAMPOS_BASE.items():
            existentes = {f.name for f in modelo._meta.get_fields()}
            for campo in campos:
                with self.subTest(modelo=modelo.__name__, campo=campo):
                    self.assertIn(
                        campo, existentes,
                        f"{modelo.__name__}.{campo} es un CAMPO BASE: otro módulo lo usa. "
                        "No lo borres ni le cambies el nombre.",
                    )

    def test_los_datos_de_prueba_se_cargan_dos_veces_sin_duplicar(self):
        call_command("cargar_datos_demo", verbosity=0)
        cantidades = [m.objects.count() for m in CAMPOS_BASE]
        call_command("cargar_datos_demo", verbosity=0)
        self.assertEqual(cantidades, [m.objects.count() for m in CAMPOS_BASE])
        self.assertGreater(Factura.objects.count(), 0)


class PantallasAbren(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("cargar_datos_demo", verbosity=0)
        cls.usuario = get_user_model().objects.create_user("prueba", password="x")

    def test_sin_sesion_redirige_al_login(self):
        respuesta = self.client.get(reverse("inicio"))
        self.assertRedirects(respuesta, "/ingresar/?next=/")

    def test_el_tablero_y_cada_modulo_abren(self):
        self.client.force_login(self.usuario)
        for nombre in ["inicio", "clientes:inicio", "productos:inicio",
                       "facturacion:inicio", "proveedores:inicio", "reportes:inicio"]:
            with self.subTest(pagina=nombre):
                self.assertEqual(self.client.get(reverse(nombre)).status_code, 200)

    def test_salud_responde_sin_login(self):
        self.assertEqual(self.client.get("/salud/").status_code, 200)
