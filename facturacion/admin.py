from django.contrib import admin

from .models import DetalleFactura, Factura


class DetalleEnLinea(admin.TabularInline):
    model = DetalleFactura
    extra = 1


@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ["id", "cliente", "fecha", "total"]
    list_filter = ["fecha"]
    inlines = [DetalleEnLinea]
