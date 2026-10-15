from django.contrib import admin

from .models import Proveedor


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "categoria", "tipo", "contacto", "telefono"]
    list_filter = ["categoria", "tipo"]
    search_fields = ["nombre", "nit", "contacto"]
    filter_horizontal = ["productos"]
