from django.db import models

# Create your models here.
class MensajeContacto(models.Model):
    # atributos
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200, blank=True, null=True)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-fecha_envio']
    
    def __str__(self):
        return f"{self.nombre} - {self.asunto or 'Sin Asunto'}"