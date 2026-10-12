from django.shortcuts import render

from .models import Cliente


def inicio(request):
    """Página inicial del módulo. Hoy solo lista; tu trabajo es mejorarla."""
    clientes = Cliente.objects.all()
    return render(request, "clientes/inicio.html", {"clientes": clientes})
