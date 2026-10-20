from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "nit", "imagen"]   # ✅ AGREGADO "imagen"
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
            "imagen": forms.ClearableFileInput(attrs={
                "class": "form-control",
                "accept": "image/*",
            }),
        }
        labels = {
            "nombre": "Nombre o razón social",
            "nit": "NIT / CI",
            "imagen": "Imagen / Logo",
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

    def clean_imagen(self):
        imagen = self.cleaned_data.get("imagen")
        # Solo valida si se subió un archivo nuevo
        if imagen and hasattr(imagen, "size"):
            if imagen.size > 2 * 1024 * 1024:  # 2 MB
                raise forms.ValidationError(
                    "La imagen no puede superar los 2 MB."
                )
            if not imagen.content_type.startswith("image/"):
                raise forms.ValidationError(
                    "El archivo debe ser una imagen (jpg, png, etc.)."
                )
        return imagen