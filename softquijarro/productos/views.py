from django.shortcuts import render

from .models import Producto


def inicio(request):
    """Página inicial del módulo. Hoy solo lista; tu trabajo es mejorarla."""
    productos = Producto.objects.all()
    return render(request, "productos/inicio.html", {"productos": productos})
