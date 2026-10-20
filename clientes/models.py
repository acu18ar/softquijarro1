from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models


class PhotosStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('location', settings.BASE_DIR / 'clientes' / 'Photos')
        kwargs.setdefault('base_url', '/clientes/photos/')   # ⚠️ CAMBIO
        super().__init__(*args, **kwargs)


class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    nit = models.CharField(max_length=50)
    imagen = models.ImageField(
        upload_to='',
        storage=PhotosStorage(),
        null=True,
        blank=True,
        verbose_name='Imagen / Logo',
    )

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.nit})'