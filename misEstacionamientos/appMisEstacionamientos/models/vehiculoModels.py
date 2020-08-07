from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from appMisEstacionamientos.models.helperModels import Color, Marca
from django.core.validators import MaxValueValidator, MinValueValidator


# Vehiculo
# Clase que representa un vehiculo de un usuario.
class Vehiculo(models.Model):
    patente = models.CharField(max_length=8)
    anio = models.PositiveIntegerField(
        default=2019, verbose_name='Año',
        validators=[MinValueValidator(1900), MaxValueValidator(2019)])
    color = models.ForeignKey(
        Color, on_delete=models.SET_NULL, null=True, help_text='Seleccione un color')
    marca = models.ForeignKey(
        Marca, on_delete=models.SET_NULL, null=True, help_text='Seleccione una marca')
    modelo = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class meta:
        ordering = ('anio',)

    def get_absolute_url(self):
        return reverse('verVehiculo', args=[self.id])

    def get_update_url(self):
        return reverse('editarVehiculo', args=[self.id])

    def get_delete_url(self):
        return reverse('eliminarVehiculo', args=[self.id])

    def __str__(self):
        return self.patente + ' ' + self.anio
