from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    titulo= models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' - ' + self.usuario.username

    class Meta:
        ordering = ['-fecha_creacion']  