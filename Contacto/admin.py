from django.contrib import admin
from .models import MensajeContacto
# Register your models here.
@admin.register(MensajeContacto)

class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'mensaje',  'fecha_envio')
    search_fields = ('nombre', 'email', 'asunto', 'fecha_envio', 'mensaje')
    list_filter = ('fecha_envio',)
    rendoly_fields = {'nombre', 'email', 'asunto', 'fecha_envio', 'mensaje'}
    
    fieldsets = (
        ('Datos del remitente', {'fields': ('nombre', 'email')} ),
        ('Mensaje', {'fields': ('asunto', 'mensaje')} ),
        ('Información adicional', {'fields': ('fecha_envio',), 'classes': ('collapse',), 'classes': ('collapse',)} ),
    )
    
    def has_add_permission(self, request):
        return False