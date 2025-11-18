from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import MensajeContacto
# Create your views here.

def contacto_view(request):
    # variable bandera
    mensaje_enviado = False
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        
        # guardar el mensaje en la base de datos
        MensajeContacto.objects.create(
            nombre=nombre,
            email=email,
            asunto=asunto,
            mensaje=mensaje,
        )
        
        # enviar correo admin
        cuerpo = f"""
            Nuevo mensaje recibido desde el formulario de contacto:
            
            Nombre: {nombre}
            Email: {email}
            Asunto: {asunto}
            
            Mensaje:
            {mensaje}
        """
        
        send_mail(
            subject=f"contacto: {asunto or 'sin asunto'}",
            message=cuerpo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['yepessamuel171@gmail.com'],# reemplaza con tu correo
        )
        
        # correo de confirmacion al usuario
        confirmacion = f"Hola {nombre},\n\n Hemos recibido tu mensaje"
        send_mail(
            subject=f"Confirmación de recepción de mensaje",
            message=cuerpo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],# reemplaza con tu correo
        )
        
        mensaje_enviado = True
        
    return render(request, 'contacto.html', {'mensaje_enviado': mensaje_enviado})