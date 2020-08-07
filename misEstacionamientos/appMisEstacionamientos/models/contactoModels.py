from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator


# Contacto:
# Clase que permite el ingreso de sugerencias y cosas por el estilo.
class Contacto(models.Model):
    nombre = models.CharField(
        max_length=30, 
        help_text='Ingrese su nombre')
    email = models.CharField(
        max_length=75, 
        help_text='Ingrese su email')
    mensaje = models.TextField(
        max_length=250, 
        help_text='Ingrese su mensaje')

    class meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre