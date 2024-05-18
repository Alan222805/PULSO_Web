from django.shortcuts import render
from Productos.models import Imagen_producto

# Create your views here.

def home (request):
    return render(request, 'Inicio.html')

def Comun (request):
    return render(request, 'Comun.html')

def sobre_nosotros (request):
    return render(request, 'sobre_nosotros.html')


