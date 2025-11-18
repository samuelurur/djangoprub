from django.db import models
from Servicios.models import Servicio  # Importa tu modelo Servicio
from Empleados.models import Empleado  # Importa tu modelo Empleado

# Horas disponibles para las citas
TIME_CHOICES = (
    ("09:00", "09:00 AM"),
    ("10:00", "10:00 AM"),
    ("11:00", "11:00 AM"),
    ("12:00", "12:00 PM"),
    ("13:00", "01:00 PM"),
    ("14:00", "02:00 PM"),
    ("15:00", "03:00 PM"),
    ("16:00", "04:00 PM"),
    ("17:00", "05:00 PM"),
)

class Cita(models.Model):
    # Datos del cliente
    nombre = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=15)
    
    # Datos de la cita (Relaciones con otras apps)
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    
    fecha = models.DateField()
    hora = models.CharField(max_length=5, choices=TIME_CHOICES, default="09:00")
    
    notas = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ['-fecha', '-hora']

    def __str__(self):
        return f"Cita para {self.nombre} el {self.fecha} a las {self.hora}"