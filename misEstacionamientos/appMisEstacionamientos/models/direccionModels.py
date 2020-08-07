from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from appMisEstacionamientos.models.helperModels import TipoDireccion, TipoVivienda, Comuna


# Direccion
# Clase que representa una direccion del usuario.
class Direccion(models.Model):
    tipo_direccion = models.ForeignKey(
        TipoDireccion, on_delete=models.SET_NULL, null=True, help_text='Seleccione tipo de dirección')
    direccion = models.CharField(max_length=50)
    numero = models.CharField(max_length=10, null=True, blank=True)
    tipo_vivienda = models.ForeignKey(
        TipoVivienda, on_delete=models.SET_NULL, null=True, help_text='Seleccione tipo de vivienda')
    piso = models.CharField(max_length=6, null=True, blank=True)
    departamento = models.CharField(max_length=10, null=True, blank=True)
    villa_poblacion = models.CharField(max_length=50, null=True, blank=True)
    comuna = models.ForeignKey(
        Comuna, on_delete=models.SET_NULL, null=True, help_text='Seleccione una comuna')
    codigo_postal = models.CharField(max_length=8, null=True, blank=True)
    direccionLocator = models.TextField(max_length=150, null=True, blank=True)
    longitudLocator = models.DecimalField(default=0, max_digits=9, decimal_places=6)
    latitudLocator = models.DecimalField(default=0, max_digits=8, decimal_places=6)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class meta:
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse('verDireccion', args=[self.id])

    def get_update_url(self):
        return reverse('editarDireccion', args=[self.id])

    def get_delete_url(self):
        return reverse('eliminarDireccion', args=[self.id])

    def __str__(self):
        return self.direccion + ' ' + self.numero
