from django.forms import ModelForm
from appMisEstacionamientos.models.tarjetasModels import Tarjeta


# TarjetaForm:
# Formulario de registro de tarjetas de pago.
class TarjetaForm(ModelForm):
    class Meta:
        model = Tarjeta
        fields = ('tipo_tarjeta', 'banco', 'numero_tarjeta',
                  'vencimiento')
