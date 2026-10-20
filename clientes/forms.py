from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "nit"]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre o razón social",
                "autofocus": True,
            }),
            "nit": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "NIT / CI",
            }),
        }
        labels = {
            "nombre": "Nombre o razón social",
            "nit": "NIT / CI",
        }

    def clean_nombre(self):
        nombre = (self.cleaned_data.get("nombre") or "").strip()
        if not nombre:
            raise forms.ValidationError("El nombre o razón social es obligatorio.")
        return nombre

    def clean_nit(self):
        nit = (self.cleaned_data.get("nit") or "").strip()
        if not nit:
            raise forms.ValidationError("El NIT/CI es obligatorio.")
        return nit