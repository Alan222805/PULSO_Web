from django.shortcuts import render
from .models import Imagen_producto, productos

def products (request):
    producto = productos.objects.all().prefetch_related('imagenes').order_by('id')
    return render(request, 'Productos.html', {'products': producto})
