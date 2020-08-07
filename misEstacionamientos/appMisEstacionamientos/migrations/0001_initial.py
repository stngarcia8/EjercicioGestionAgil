# Generated by Django 2.1.7 on 2019-06-25 05:22

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nombre_web', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese su nombre', max_length=30)),
                ('email', models.CharField(help_text='Ingrese su email', max_length=75)),
                ('mensaje', models.TextField(help_text='Ingrese su mensaje', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('piso', models.CharField(blank=True, max_length=6, null=True)),
                ('departamento', models.CharField(blank=True, max_length=10, null=True)),
                ('villa_poblacion', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=8, null=True)),
                ('direccionLocator', models.TextField(blank=True, max_length=150, null=True)),
                ('longitudLocator', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('latitudLocator', models.DecimalField(decimal_places=6, default=0, max_digits=8)),
                ('comuna', models.ForeignKey(help_text='Seleccione una comuna', null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMisEstacionamientos.Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDescriptivo', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^([A-Za-zÑñ\\-]{3,})[\\s]{0,1}([A-Za-zÑñ\\-]{0,})$')], verbose_name='NombreDescriptivo')),
                ('precioEstacionamiento', models.IntegerField(validators=[django.core.validators.RegexValidator('^([A-Za-zÑñ\\-]{3,})[\\s]{0,1}([A-Za-zÑñ\\-]{0,})$')], verbose_name='PrecioEstacionamiento')),
                ('disponibilidadEstacionamiento', models.BooleanField(default=False)),
                ('descripcionEstacionamiento', models.TextField(blank=True, max_length=100, null=True, verbose_name='DescripcionEstacionamiento')),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appMisEstacionamientos.Direccion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator('^([A-Za-zÑñ\\-]{3,})[\\s]{0,1}([A-Za-zÑñ\\-]{0,})$')], verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^([A-Za-zÑñ\\-]{3,})[\\s]{0,1}([A-Za-zÑñ\\-]{0,})$')], verbose_name='Apellidos')),
                ('rut', models.CharField(help_text='(ej: 12345678-9)', max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^([0-9]{6,8}-[0-9Kk])$')], verbose_name='Rut')),
                ('nacimiento', models.DateField(default=datetime.date.today, help_text='Formato: dd/mm/aaaa', verbose_name='Fecha Nacimiento')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.RegexValidator('^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$')])),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_tarjeta', models.CharField(max_length=20)),
                ('vencimiento', models.CharField(blank=True, max_length=5, null=True)),
                ('banco', models.ForeignKey(help_text='Seleccione banco', null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMisEstacionamientos.Banco')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDireccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='TipoTarjeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='TipoVivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=8)),
                ('anio', models.PositiveIntegerField(default=2019, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2019)], verbose_name='Año')),
                ('modelo', models.CharField(max_length=50)),
                ('color', models.ForeignKey(help_text='Seleccione un color', null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMisEstacionamientos.Color')),
                ('marca', models.ForeignKey(help_text='Seleccione una marca', null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMisEstacionamientos.Marca')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='tipo_tarjeta',
            field=models.ForeignKey(help_text='Seleccione tipo de tarjeta', null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMisEstacionamientos.TipoTarjeta'),
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='direccion',
            name='tipo_direccion',
            field=models.ForeignKey(help_text='Seleccione tipo de dirección', null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMisEstacionamientos.TipoDireccion'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='tipo_vivienda',
            field=models.ForeignKey(help_text='Seleccione tipo de vivienda', null=True, on_delete=django.db.models.deletion.SET_NULL, to='appMisEstacionamientos.TipoVivienda'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]