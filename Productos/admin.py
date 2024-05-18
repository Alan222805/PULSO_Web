from django.contrib import admin
from Productos.models import productos, categoria_de_producto, producto_categoria, Imagen_producto
from Cursos.models import curso, categoria_de_curso, curso_categoria


# Register your models here.

admin.site.register(productos)
admin.site.register(categoria_de_producto)
admin.site.register(producto_categoria)
admin.site.register(Imagen_producto)

admin.site.register(curso)
admin.site.register(categoria_de_curso)
admin.site.register(curso_categoria)
