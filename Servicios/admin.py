from django.contrib import admin
from .models import Servicio  # Importa el modelo

# Registra el modelo 'Servicio'

class ServicioAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la vista de lista del admin
    list_display = ('id','titulo', 'contenido', 'imagen', 'precio',  'created', 'updated')
    
    # Campos que solo se leen y se actualizan automáticamente
    readonly_fields = ('created', 'updated')
admin.site.register(Servicio, ServicioAdmin)