from django import forms

from .models import Proveedor


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            "nombre", "nit", "tipo", "categoria", "logo_url",
            "contacto", "telefono", "correo", "direccion",
        ]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Ej. Materiales El Constructor"}),
            "nit": forms.TextInput(attrs={"placeholder": "Número de identificación tributaria o personal"}),
            "logo_url": forms.URLInput(attrs={"placeholder": "https://… (enlace a la imagen del logo)"}),
            "tipo": forms.RadioSelect,
            "contacto": forms.TextInput(attrs={"placeholder": "Ej. Juan Pérez"}),
            "telefono": forms.TextInput(attrs={"placeholder": "Ej. 7XXXXXXX"}),
            "correo": forms.EmailInput(attrs={"placeholder": "proveedor@ejemplo.com"}),
            "direccion": forms.TextInput(attrs={"placeholder": "Calle, avenida o zona"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # El teléfono es obligatorio en el formulario (en la base sigue siendo opcional).
        self.fields["telefono"].required = True
        for nombre, campo in self.fields.items():
            if nombre == "categoria":
                campo.widget.attrs["class"] = "form-select"
            elif nombre != "tipo":
                campo.widget.attrs["class"] = "form-control"

    def clean_telefono(self):
        telefono = self.cleaned_data["telefono"].strip()
        if not any(c.isdigit() for c in telefono):
            raise forms.ValidationError("Ingresa un número de teléfono válido.")
        return telefono
