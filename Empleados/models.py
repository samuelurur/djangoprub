from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='empleados', null=True, blank=True)
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_contratacion = models.DateField()

    def __str__(self):
        return self.nombre