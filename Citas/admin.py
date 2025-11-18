from django.contrib import admin
from .models import Cita

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    """
    Configuración para mostrar el modelo de Citas en el panel de admin.
    """
    
    # Campos que se mostrarán en la lista de citas
    list_display = (
        'nombre', 
        'servicio', 
        'empleado', 
        'fecha', 
        'hora'
    )
    
    # Filtros que aparecerán en la barra lateral derecha
    list_filter = (
        'fecha', 
        'empleado', 
        'servicio'
    )
    
    # Campos por los que se podrá buscar
    search_fields = (
        'nombre', 
        'email', 
        'telefono', 
        'servicio__nombre', 
        'empleado__nombre'
    )
    
    # Campos que no se pueden editar (como la fecha de creación)
    readonly_fields = ('fecha_creacion',)
    
    # Organiza los campos dentro de la vista de detalle de la cita
    fieldsets = (
        ('Información del Cliente', {
            'fields': ('nombre', 'email', 'telefono')
        }),
        ('Detalles de la Cita', {
            'fields': ('servicio', 'empleado', 'fecha', 'hora', 'notas')
        }),
        ('Metadatos', {
            'fields': ('fecha_creacion',),
            'classes': ('collapse',) # Oculta esta sección por defecto
        }),
    )