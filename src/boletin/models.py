from django.db import models

# Create your models here.

class Registro(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=7)
    celular = models.CharField(max_length=10)
    timeslamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.correo

    def __str__(self):
        return self.correo