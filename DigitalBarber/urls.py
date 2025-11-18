"""
URL configuration for DigitalBarber project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# digitalbarber/urls.py (CORREGIDO)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DigitalBarberApp.urls')),
    
    # ¡CORRECCIÓN CLAVE! Usar minúsculas:
    path('servicios/', include('Servicios.urls')),
    path('barberos/', include('Empleados.urls')),
    path('citas/', include('Citas.urls')),
    path('tienda/', include('Tienda.urls', namespace='Tienda')),
    path('nomina/', include('Nomina.urls')),
    path('contacto/', include('Contacto.urls')),
] 
# El código de configuración de media y estáticos va A CONTINUACIÓN.
# digitalbarber/urls.py (Añadir al final)

# ... (tu urlpatterns definido arriba)

if settings.DEBUG:
    # IMPORTANTE: Asegúrate de que MEDIA_URL y MEDIA_ROOT estén definidos en settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Recomendado también para archivos estáticos, aunque es menos común
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)