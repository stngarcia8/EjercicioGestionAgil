from django.forms import ModelForm
from appMisEstacionamientos.models.estacionamientoModels import Estacionamiento


# DireccionForm:
# Formulario de registro de direcciones.
class EstacionamientosForm(ModelForm):
    class Meta:
        model = Estacionamiento
        fields = ('nombreDescriptivo', 'direccion', 'precioEstacionamiento',
                  'descripcionEstacionamiento')
