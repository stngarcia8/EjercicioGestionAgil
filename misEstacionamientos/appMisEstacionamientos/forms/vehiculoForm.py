from django.forms import ModelForm
from appMisEstacionamientos.models.vehiculoModels import Vehiculo


# VehiculoForm:
# Formulario de registro de vehiculos.
class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ('patente', 'anio', 'color', 'marca', 'modelo')
