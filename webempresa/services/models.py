from django.db import models

import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']
    
    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Service)
def delete_image_on_object_delete(sender, instance, **kwargs):
    """
    Borra la imagen asociada cuando un objeto Project es eliminado.
    """
    if instance.image:
        if os.path.isfile(instance.image.path):  # Verifica si la imagen existe en el sistema de archivos
            os.remove(instance.image.path)
