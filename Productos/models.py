from django.db import models

# Create your models here.

class productos(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()
    url_producto = models.TextField(null=True)
    imagen = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class categoria_de_producto(models.Model):
    name = models.CharField(max_length=150)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class producto_categoria(models.Model):
    idProducto = models.ForeignKey(productos, on_delete=models.CASCADE)
    idCategoriaProducto = models.ForeignKey('categoria_de_producto', on_delete=models.CASCADE)
    
    
class Imagen_producto(models.Model):
    idProducto = models.ForeignKey(productos, on_delete=models.CASCADE, related_name='imagenes')
    url_imagen_producto = models.TextField(null=True)
    tipo = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.url_imagen_producto
    
    
