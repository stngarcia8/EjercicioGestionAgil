from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from appMisEstacionamientos.models.helperModels import Banco, TipoTarjeta


# Tarjeta
# Clase que representa una tarjeta de pago del usuario.
class Tarjeta(models.Model):
    tipo_tarjeta = models.ForeignKey(
        TipoTarjeta, on_delete=models.SET_NULL, null=True, help_text='Seleccione tipo de tarjeta')
    banco = models.ForeignKey(
        Banco, on_delete=models.SET_NULL, null=True, help_text='Seleccione banco')
    numero_tarjeta = models.CharField(max_length=20)
    vencimiento = models.CharField(max_length=5, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class meta:
        ordering = ('banco.nombre',)

    def get_absolute_url(self):
        return reverse('verTarjeta', args=[self.id])

    def get_update_url(self):
        return reverse('editarTarjeta', args=[self.id])

    def get_delete_url(self):
        return reverse('eliminarTarjeta', args=[self.id])

    def __str__(self):
        return self.tipo_tarjeta.nombre + ' () ' + self.banco.nombre + ')'
