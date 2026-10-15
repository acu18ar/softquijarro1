from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Cliente
from .forms import ClienteForm


@login_required
def inicio(request):
    """Página inicial del módulo. Lista los clientes y da acceso a gestionar."""
    clientes = Cliente.objects.all().order_by("nombre")
    return render(request, "clientes/inicio.html", {
        "clientes": clientes,
        "total": clientes.count(),
    })


@login_required
def gestionar(request):
    cliente_editar = None

    if request.method == "POST":
        accion = request.POST.get("accion")

        if accion == "crear":
            form = ClienteForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Cliente creado correctamente.")
                return redirect("clientes:gestionar")
            messages.error(request, "Revisa los errores del formulario.")

        elif accion == "editar":
            pk = request.POST.get("id")
            cliente = get_object_or_404(Cliente, pk=pk)
            form = ClienteForm(request.POST, instance=cliente)
            if form.is_valid():
                form.save()
                messages.success(request, "Cliente actualizado correctamente.")
                return redirect("clientes:gestionar")
            messages.error(request, "Revisa los errores del formulario.")
            cliente_editar = cliente

        elif accion == "eliminar":
            pk = request.POST.get("id")
            cliente = get_object_or_404(Cliente, pk=pk)
            nombre = cliente.nombre
            cliente.delete()
            messages.success(request, f"Cliente '{nombre}' eliminado correctamente.")
            return redirect("clientes:gestionar")

    else:
        form = ClienteForm()

    clientes = Cliente.objects.all().order_by("nombre")

    return render(request, "clientes/gestionar.html", {
        "clientes": clientes,
        "form": form,
        "cliente_editar": cliente_editar,
    })