from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from appMisEstacionamientos.forms.direccionForm import DireccionForm
from .direccionModels import Direccion
from django.urls import reverse


# Estacionamientos
# Clase que representa un estacionamiento
class Estacionamiento(models.Model):
    nombreDescriptivo = models.CharField(
        max_length=30,
        verbose_name='Nombre Descriptivo')
    precioEstacionamiento = models.IntegerField(
        verbose_name='Precio Estacionamiento',
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(99999)])
    disponibilidadEstacionamiento = models.BooleanField(default=False)
    descripcionEstacionamiento = models.TextField(
        max_length=100,
        verbose_name='Descripcion Estacionamiento',
        null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    class meta:
        ordering = ('nombreDescriptivo',)

    def get_absolute_url(self):
        return reverse('verEstacionamiento', args=[self.id])

    def get_update_url(self):
        return reverse('editarEstacionamiento', args=[self.id])

    def get_delete_url(self):
        return reverse('eliminarEstacionamiento', args=[self.id])

    def get_enable_url(self):
        return reverse('habilitarEstacionamiento', args=[self.id])

    def get_disable_url(self):
        return reverse('inhabilitarEstacionamiento', args=[self.id])

    def __str__(self):
        return self.nombreDescriptivo
