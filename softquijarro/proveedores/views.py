from django.shortcuts import render

from .models import Proveedor


def inicio(request):
    """Página inicial del módulo. Hoy solo lista; tu trabajo es mejorarla."""
    proveedores = Proveedor.objects.all()
    return render(request, "proveedores/inicio.html", {"proveedores": proveedores})
