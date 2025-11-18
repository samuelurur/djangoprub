from django.contrib import admin
from .models import PagoNomina  # 1. Importa el modelo

# 2. Registra el modelo 'PagoNomina'
@admin.register(PagoNomina)
class PagoNominaAdmin(admin.ModelAdmin):
    # Opcional: Esto mejora mucho la vista de admin para nóminas
    
    # Muestra estos campos en la lista
    list_display = ('empleado', 'fecha_pago', 'monto')
    
    # Añade filtros útiles en el lateral
    list_filter = ('fecha_pago', 'empleado')
    
    # Permite buscar por el nombre del empleado (usando __nombre para el ForeignKey)
    search_fields = ('empleado__nombre',)