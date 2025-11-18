from django.contrib import admin
from .models import Empleado  # Importa el modelo

# Registra el modelo 'Empleado'
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    # Opcional: Personaliza la vista de lista en el admin
    list_display = ('nombre', 'puesto', 'salario', 'fecha_contratacion')
    
    # Añade filtros por puesto o fecha de contratación
    list_filter = ('puesto', 'fecha_contratacion')
    
    # Permite buscar por nombre o puesto
    search_fields = ('nombre', 'puesto')