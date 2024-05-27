from django.shortcuts import render, get_object_or_404
from .models import Imagen_producto, productos

def products (request):
    producto = productos.objects.all().prefetch_related('imagenes').order_by('id')
    return render(request, 'Productos.html', {'products': producto})

def producto_detalle (request, id):
    producto = get_object_or_404(productos, id=id)
    imagenes = Imagen_producto.objects.filter(idProducto=id)
    return render(request, 'producto_detalle.html', {'producto': producto, 'imagenes': imagenes})
