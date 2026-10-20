from django.shortcuts import render
from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.db.models import Sum

from clientes.models import Cliente
from productos.models import Producto
from .models import Factura, DetalleFactura




def inicio(request):
    facturas = Factura.objects.select_related("cliente").all()

    total_facturado = (
        Factura.objects.aggregate(total=Sum("total"))["total"] or 0
    )

    return render(
        request,
        "facturacion/inicio.html",
        {
            "facturas": facturas,
            "total_facturado": total_facturado,
        },
    )
def nueva(request):
    clientes = Cliente.objects.all().order_by("nombre")
    productos = Producto.objects.all().order_by("nombre")

    if request.method == "POST":
        cliente_id = request.POST.get("cliente")
        productos_ids = request.POST.getlist("producto")
        cantidades = request.POST.getlist("cantidad")

        if not cliente_id:
            messages.error(request, "Selecciona un cliente.")
            return redirect("facturacion:nueva")

        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except (Cliente.DoesNotExist, ValueError, TypeError):
            messages.error(request, "El cliente seleccionado no es válido.")
            return redirect("facturacion:nueva")

        lineas = []

        for producto_id, cantidad_texto in zip(productos_ids, cantidades):
            if not producto_id:
                continue

            try:
                producto_id = int(producto_id)
                cantidad = int(cantidad_texto)
            except (ValueError, TypeError):
                messages.error(request, "Revisa los productos y las cantidades.")
                return redirect("facturacion:nueva")

            if cantidad < 1:
                messages.error(request, "La cantidad debe ser mayor que cero.")
                return redirect("facturacion:nueva")

            lineas.append((producto_id, cantidad))

        if not lineas:
            messages.error(request, "Agrega al menos un producto.")
            return redirect("facturacion:nueva")

        # Agrupa las cantidades si un producto aparece varias veces.
        cantidades_por_producto = {}
        for producto_id, cantidad in lineas:
            cantidades_por_producto[producto_id] = (
                cantidades_por_producto.get(producto_id, 0) + cantidad
            )

        try:
            with transaction.atomic():
                productos_bloqueados = (
                    Producto.objects.select_for_update()
                    .filter(pk__in=cantidades_por_producto.keys())
                )
                productos_por_id = {
                    producto.pk: producto
                    for producto in productos_bloqueados
                }

                if len(productos_por_id) != len(cantidades_por_producto):
                    raise ValueError(
                        "Uno de los productos seleccionados ya no existe."
                    )

                # Verifica todo el stock antes de guardar la factura.
                for producto_id, cantidad_total in cantidades_por_producto.items():
                    producto = productos_por_id[producto_id]

                    if producto.stock < cantidad_total:
                        raise ValueError(
                            f"Stock insuficiente para {producto.nombre}. "
                            f"Disponible: {producto.stock}."
                        )

                factura = Factura.objects.create(
                    cliente=cliente,
                    total=0,
                )

                total = 0

                # Guarda cada línea con el precio actual del inventario.
                for producto_id, cantidad in lineas:
                    producto = productos_por_id[producto_id]

                    DetalleFactura.objects.create(
                        factura=factura,
                        producto=producto,
                        cantidad=cantidad,
                        precio_unitario=producto.precio,
                    )

                    total += producto.precio * cantidad

                # Descuenta el stock una vez por producto.
                for producto_id, cantidad_total in cantidades_por_producto.items():
                    producto = productos_por_id[producto_id]
                    producto.stock -= cantidad_total
                    producto.save(update_fields=["stock"])

                factura.total = total
                factura.save(update_fields=["total"])

        except ValueError as error:
            messages.error(request, str(error))
            return redirect("facturacion:nueva")

        messages.success(request, "La factura se guardó correctamente.")
        return redirect("facturacion:detalle", pk=factura.pk)

    return render(
        request,
        "facturacion/nueva.html",
        {
            "clientes": clientes,
            "productos": productos,
        },
    )


def detalle(request, pk):
    factura = get_object_or_404(
        Factura.objects.select_related("cliente").prefetch_related(
            "detalles__producto"
        ),
        pk=pk,
    )
    return render(
        request,
        "facturacion/detalle.html",
        {"factura": factura},
    )


def imprimir(request, pk):
    factura = get_object_or_404(
        Factura.objects.select_related("cliente").prefetch_related(
            "detalles__producto"
        ),
        pk=pk,
    )
    return render(
        request,
        "facturacion/imprimir.html",
        {"factura": factura},
    )
