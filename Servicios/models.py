from django.db import models

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios')
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.titulo
