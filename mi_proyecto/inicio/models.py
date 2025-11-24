from django.db import models

# Create your models here.


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Mejora(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    sugerencia = models.TextField()
    prioridad = models.CharField(
        max_length=10,
        choices=[
            ('baja', 'Baja'),
            ('media', 'Media'),
            ('alta', 'Alta'),
        ]
    )
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.prioridad}"
