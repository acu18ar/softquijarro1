from django.http import JsonResponse
from django.shortcuts import render


def inicio(request):
    """Tablero principal: una tarjeta por módulo, tomada del menú."""
    return render(request, "core/inicio.html")


def salud(request):
    """Responde 'ok' sin pedir login. Render lo usa para saber si la app vive."""
    return JsonResponse({"estado": "ok"})
