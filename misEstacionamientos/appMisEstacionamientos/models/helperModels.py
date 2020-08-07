from django.db import models


# Color
# Clase que define un color.
class Color(models.Model):
    nombre = models.CharField(max_length=50)
    nombre_web = models.CharField(max_length=50)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre + ' (' + self.nombre_web + ')'


# Marca
# Clase que define una marca de vehiculo.
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# TipoVivienda
# Clase que define un tipo de vivienda.
class TipoVivienda(models.Model):
    nombre = models.CharField(max_length=20)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# TipoDireccion
# Clase que define un tipo de direccion.
class TipoDireccion(models.Model):
    nombre = models.CharField(max_length=15)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# Comuna
# Clase que define una comuna.
class Comuna(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# Banco
# Clase que define un banco.
class Banco(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


# TipoTarjeta
# Clase que define un tipo de tarjeta.
class TipoTarjeta(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre
