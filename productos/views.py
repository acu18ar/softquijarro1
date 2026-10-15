from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def inicio(request):
    """Lista los productos, con búsqueda por nombre y filtro por categoría."""
    q = request.GET.get("q", "").strip()
    categoria = request.GET.get("categoria", "").strip()

    productos = Producto.objects.all()

    if q:
        productos = productos.filter(nombre__icontains=q)
    if categoria:
        productos = productos.filter(categoria=categoria)

    productos_bajos = [p for p in productos if p.stock_bajo]

    return render(request, "productos/inicio.html", {
        "productos": productos,
        "productos_bajos": productos_bajos,
        "total_bajos": len(productos_bajos),
        "categorias": Producto.CATEGORIA_CHOICES,
        "q": q,
        "categoria_actual": categoria,
    })


def crear_producto(request):
    """Muestra el formulario y guarda un producto nuevo."""
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" agregado correctamente.')
            return redirect("productos:inicio")
        messages.error(request, "Revisa los errores del formulario.")
    else:
        form = ProductoForm()
    return render(request, "productos/crear_producto.html", {
        "form": form,
        "titulo": "Agregar producto",
    })


def editar_producto(request, pk):
    """Edita un producto existente."""
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado.')
            return redirect("productos:inicio")
        messages.error(request, "Revisa los errores del formulario.")
    else:
        form = ProductoForm(instance=producto)
    return render(request, "productos/crear_producto.html", {
        "form": form,
        "titulo": f"Editar: {producto.nombre}",
        "producto": producto,
    })


def eliminar_producto(request, pk):
    """Elimina un producto (con confirmación)."""
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado.')
        return redirect("productos:inicio")
    return render(request, "productos/eliminar_producto.html", {"producto": producto})