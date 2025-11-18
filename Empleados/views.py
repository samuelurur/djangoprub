from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Empleado

# Create your views here.
def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/empleados.html', {'empleados': empleados})