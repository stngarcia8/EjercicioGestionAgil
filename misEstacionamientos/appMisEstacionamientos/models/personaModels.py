from django.contrib.auth.models import User
from django.db import models

from django.urls import reverse
import datetime
from django.core.validators import RegexValidator


# Persona
# Clase que representa una persona
class Persona(models.Model):
    nombre = models.CharField(
        max_length=25,
        verbose_name='Nombre',
        validators=[
            RegexValidator(r'^([A-Za-zÑñ\-]{3,})[\s]{0,1}([A-Za-zÑñ\-]{0,})$')
        ])
    apellido = models.CharField(
        max_length=30,
        verbose_name='Apellidos',
        validators=[
            RegexValidator(r'^([A-Za-zÑñ\-]{3,})[\s]{0,1}([A-Za-zÑñ\-]{0,})$')
        ])
    rut = models.CharField(
        max_length=10,
        unique=True,
        help_text='(ej: 12345678-9)',
        verbose_name='Rut',
        validators=[RegexValidator(r'^([0-9]{6,8}-[0-9Kk])$')])
    nacimiento = models.DateField(
        default=datetime.date.today,
        help_text='Formato: dd/mm/aaaa',
        verbose_name='Fecha Nacimiento')
    email = models.EmailField(validators=[
        RegexValidator(r'^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$')
    ])
    telefono = models.CharField(
        max_length=15, null=True, blank=True, verbose_name='Teléfono')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class meta:
        ordering = ('apellido', 'nombre',)

    def get_absolute_url(self):
        return reverse('verUsuario', args=[self.id])

    def get_update_url(self):
        return reverse('editarUsuario', args=[self.id])

    def get_update_credentials_url(self):
        return reverse('editarCredencialesUsuario', args=[self.usuario.id])

    def __str__(self):
        return self.direccion + ' ' + self.numero
