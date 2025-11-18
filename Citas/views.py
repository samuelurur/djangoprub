from django.shortcuts import render, redirect
from .forms import CitaForm
from django.contrib import messages


# ... (otras importaciones)

def reservar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Tu cita ha sido reservada con éxito!')
            
            # CAMBIO: Redirige a 'Citas:reservar'
            return redirect('Citas:reservar') 
    else:
        form = CitaForm() 

    return render(request, 'Citas/citas.html', {'form': form})