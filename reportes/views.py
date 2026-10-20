
from django.db.models import Count, Sum
from django.shortcuts import render

from facturacion.models import Factura


def inicio(request):
    """Página inicial del módulo. Hoy muestra un resumen; tu trabajo es ampliarla.

    Ejemplo de consulta útil para "productos más vendidos":
        from facturacion.models import DetalleFactura
        DetalleFactura.objects.values("producto__nombre") \\
            .annotate(unidades=Sum("cantidad")).order_by("-unidades")[:5]
    """
    resumen = Factura.objects.aggregate(cantidad=Count("id"), vendido=Sum("total"))
    return render(request, "reportes/inicio.html", {"resumen": resumen})

"""Vistas del módulo Reportes.

Solo lee datos de otros módulos. No crea ni modifica modelos.
Si el módulo de facturación existe, se activan los reportes de ventas.
"""
from datetime import timedelta

from django.db.models import Count, F, Sum
from django.shortcuts import render
from django.utils import timezone

from clientes.models import Cliente
from productos.models import Producto
from proveedores.models import Proveedor

# ── Detección automática del módulo de facturación ──────────────────────
try:
    from facturacion.models import DetalleFactura, Factura
    FACTURACION_LISTA = True
except (ImportError, RuntimeError):
    FACTURACION_LISTA = False


def _obtener_contexto_reporte():
    """Construye el contexto del reporte. Reutilizable por vista normal y por PDF."""
    hoy = timezone.localdate()
    hace_30_dias = hoy - timedelta(days=30)

    # ── Sección 1: Ventas del día ───────────────────────────────────────
    ventas_dia = None
    if FACTURACION_LISTA:
        facturas_hoy = Factura.objects.filter(fecha__date=hoy)
        ventas_dia = facturas_hoy.aggregate(
            cantidad=Count("id"),
            total=Sum("total"),
        )

    # ── Sección 2: Productos más vendidos ───────────────────────────────
    mas_vendidos = None
    if FACTURACION_LISTA:
        mas_vendidos = list(
            DetalleFactura.objects
            .filter(factura__fecha__date__gte=hace_30_dias)
            .values("producto__nombre")
            .annotate(unidades=Sum("cantidad"))
            .order_by("-unidades")[:10]
        )

    # ── Sección 3: Clientes frecuentes ──────────────────────────────────
    clientes_frecuentes = None
    if FACTURACION_LISTA:
        clientes_frecuentes = list(
            Factura.objects
            .values("cliente__nombre", "cliente__nit")
            .annotate(compras=Count("id"), total=Sum("total"))
            .order_by("-compras")[:10]
        )

    # ── Sección 4: Inventario ───────────────────────────────────────────
    total_productos = Producto.objects.count()
    stock_bajo = list(
        Producto.objects.filter(stock__lte=F("stock_minimo")).order_by("stock")[:20]
    )
    sin_stock = Producto.objects.filter(stock=0).count()
    valor_inventario = (
        Producto.objects.aggregate(valor=Sum(F("precio") * F("stock")))["valor"] or 0
    )
    por_categoria = list(
        Producto.objects.values("categoria")
        .annotate(cantidad=Count("id"))
        .order_by("-cantidad")
    )

    # ── Sección 5: Clientes y proveedores ───────────────────────────────
    total_clientes = Cliente.objects.count()
    total_proveedores = Proveedor.objects.count()
    top_valor = list(
        Producto.objects.annotate(valor=F("precio") * F("stock"))
        .order_by("-valor")[:5]
    )
    proveedores_con_productos = list(
        Proveedor.objects.annotate(cantidad_productos=Count("productos"))
        .order_by("-cantidad_productos")[:10]
    )

    return {
        "facturacion_lista": FACTURACION_LISTA,
        "hoy": hoy,
        "ventas_dia": ventas_dia,
        "mas_vendidos": mas_vendidos,
        "clientes_frecuentes": clientes_frecuentes,
        "total_productos": total_productos,
        "stock_bajo": stock_bajo,
        "total_stock_bajo": len(stock_bajo),
        "sin_stock": sin_stock,
        "valor_inventario": valor_inventario,
        "por_categoria": por_categoria,
        "top_valor": top_valor,
        "total_clientes": total_clientes,
        "total_proveedores": total_proveedores,
        "proveedores_con_productos": proveedores_con_productos,
    }


def inicio(request):
    """Dashboard principal con todas las secciones del backlog."""
    return render(request, "reportes/inicio.html", _obtener_contexto_reporte())


def reporte_imprimible(request):
    """Vista lista para imprimir o guardar como PDF desde el navegador."""
    return render(request, "reportes/reporte_imprimible.html", _obtener_contexto_reporte())
