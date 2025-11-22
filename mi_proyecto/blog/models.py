from django.db import models


class Post(models.Model):
  # Atributos
    titulo = models.CharField(max_length=70, null=False)
    contenido = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
