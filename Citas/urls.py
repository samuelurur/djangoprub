# En Citas/urls.py

from django.urls import path
from . import views

# Asignamos el nombre de la app (namespace)
app_name = 'Citas' 

urlpatterns = [
    # CAMBIO: Renombramos 'citas' a 'reservar'
    path('', views.reservar_cita, name='reservar'), 
]