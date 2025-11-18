from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    
    # Hacemos que el campo 'fecha' use el widget de HTML5 tipo 'date'
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    
    class Meta:
        model = Cita
        fields = ['nombre', 'email', 'telefono', 'servicio', 'empleado', 'fecha', 'hora', 'notas']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Opciones para los menús desplegables
        self.fields['servicio'].empty_label = "Elige un servicio..."
        self.fields['empleado'].empty_label = "Elige tu barbero..."
        self.fields['hora'].empty_label = None # No queremos un "vacío" en la hora
        
        # Añadir la clase .form-control a todos los campos
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.DateInput): # Ya se lo pusimos a 'fecha'
                field.widget.attrs.update({'class': 'form-control'})
                
        # Personalizar el campo de 'notas'
        self.fields['notas'].widget.attrs.update({'rows': 3})