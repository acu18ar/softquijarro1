from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProveedorForm
from .models import Proveedor


def inicio(request):
    """Lista de proveedores con búsqueda por nombre y filtro por categoría."""
    q = request.GET.get("q", "").strip()
    categoria = request.GET.get("categoria", "")
    proveedores = Proveedor.objects.prefetch_related("productos")
    if q:
        proveedores = proveedores.filter(nombre__icontains=q)
    if categoria:
        proveedores = proveedores.filter(categoria=categoria)
    return render(request, "proveedores/inicio.html", {
        "proveedores": proveedores,
        "q": q,
        "categoria": categoria,
        "categorias": Proveedor.CATEGORIAS,
    })


def crear(request):
    form = ProveedorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        proveedor = form.save()
        messages.success(request, f"Proveedor «{proveedor.nombre}» registrado.")
        return redirect("proveedores:detalle", pk=proveedor.pk)
    return render(request, "proveedores/form.html", {"form": form, "titulo": "Nuevo proveedor"})


def editar(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    form = ProveedorForm(request.POST or None, instance=proveedor)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Proveedor «{proveedor.nombre}» actualizado.")
        return redirect("proveedores:detalle", pk=proveedor.pk)
    return render(request, "proveedores/form.html", {
        "form": form, "titulo": "Editar proveedor", "proveedor": proveedor,
    })


def detalle(request, pk):
    """Ficha del proveedor: sus datos y los productos que surte con su stock."""
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, "proveedores/detalle.html", {
        "proveedor": proveedor,
        "productos": proveedor.productos.all(),
    })


def eliminar(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        nombre = proveedor.nombre
        proveedor.delete()
        messages.success(request, f"Proveedor «{nombre}» eliminado.")
        return redirect("proveedores:inicio")
    return render(request, "proveedores/confirmar_eliminar.html", {"proveedor": proveedor})
