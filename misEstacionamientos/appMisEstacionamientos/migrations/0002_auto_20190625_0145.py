# Generated by Django 2.1.7 on 2019-06-25 05:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMisEstacionamientos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacionamiento',
            name='descripcionEstacionamiento',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Descripcion Estacionamiento'),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='nombreDescriptivo',
            field=models.CharField(max_length=30, verbose_name='Nombre Descriptivo'),
        ),
        migrations.AlterField(
            model_name='estacionamiento',
            name='precioEstacionamiento',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99999)], verbose_name='Precio Estacionamiento'),
        ),
    ]
