from __future__ import unicode_literals

from django.db import models

#Crear tú modelo aquí
class Regitro(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.constraints()
    celular = models.constraints()
    timeslamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.email

    def __str__(self):
        return self.email


