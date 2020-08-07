from django.forms import ModelForm
from appMisEstacionamientos.models.direccionModels import Direccion


# DireccionForm:
# Formulario de registro de direcciones.
class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ('tipo_direccion', 'direccion', 'numero',
                  'tipo_vivienda', 'piso', 'departamento',
                  'villa_poblacion', 'comuna', 'codigo_postal')
