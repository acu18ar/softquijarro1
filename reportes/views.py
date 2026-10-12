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
