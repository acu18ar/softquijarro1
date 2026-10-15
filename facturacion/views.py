from django.shortcuts import render

from .models import Factura


def inicio(request):
    """Página inicial del módulo. Hoy solo lista; tu trabajo es mejorarla."""
    facturas = Factura.objects.select_related("cliente")
    return render(request, "facturacion/inicio.html", {"facturas": facturas})
