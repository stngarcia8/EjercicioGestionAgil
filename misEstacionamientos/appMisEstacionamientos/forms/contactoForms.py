from django.forms import ModelForm
from django import forms
from appMisEstacionamientos.models.contactoModels import Contacto


#  ContactoForm:
# Clase que permite el registro de mensajes de contacto.
class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'mensaje')
