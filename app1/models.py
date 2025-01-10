from django.db import models
from django.utils.timezone import now

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)
    fecha_publicacion = models.DateField(blank=True, null=True)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    prestado_a = models.CharField(max_length=30)
    fecha_prestamo = models.DateField(default=now)
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField(default=False)

    def cambiar_disponibilidad_libro(self):
        if self.devuelto:
            self.libro.disponible = True
        else:
            self.libro.disponible = False
        self.libro.save()

    def save(self, *args, **kwargs):
        self.cambiar_disponibilidad_libro()

        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Libro {self.libro.titulo} prestado a {self.prestado_a}"