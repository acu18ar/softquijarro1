from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "categoria", "proveedor", "precio", "stock", "stock_minimo", "descripcion"]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: Cemento Viacha 50 kg",
            }),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "proveedor": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej: Materiales de Construcción El Constructor",
            }),
            "precio": forms.NumberInput(attrs={
                "class": "form-control",
                "step": "0.01",
                "min": "0",
            }),
            "stock": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "stock_minimo": forms.NumberInput(attrs={"class": "form-control", "min": "0"}),
            "descripcion": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Detalle opcional del producto",
            }),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get("precio")
        if precio is not None and precio < 0:
            raise forms.ValidationError("El precio no puede ser negativo.")
        return precio

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "").strip()
        if not nombre:
            raise forms.ValidationError("El nombre es obligatorio.")
        return nombre

    def clean(self):
        data = super().clean()
        stock = data.get("stock")
        stock_min = data.get("stock_minimo")
        if stock is not None and stock_min is not None and stock_min > stock * 2 and stock > 0:
            # Aviso suave, no bloquea. Puedes quitarlo si no lo quieres.
            pass
        return data