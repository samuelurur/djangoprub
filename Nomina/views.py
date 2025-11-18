from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def nomina(request):
    return render(request, 'nomina/nomina.html')