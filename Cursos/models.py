from django.db import models

# Create your models here.

class curso(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.IntegerField()
    url_curso = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class categoria_de_curso(models.Model):
    name = models.CharField(max_length=150)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class curso_categoria(models.Model):
    idCurso = models.ForeignKey(curso, on_delete=models.CASCADE)
    idCategoriaCurso = models.ForeignKey('categoria_de_curso', on_delete=models.CASCADE)
