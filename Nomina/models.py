from django.db import models

# Create your models here.

class PagoNomina(models.Model):
    empleado = models.ForeignKey('Empleados.Empleado', on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pago de {self.empleado.nombre} el {self.fecha_pago}'