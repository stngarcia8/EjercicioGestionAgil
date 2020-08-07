from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView
from django.urls import reverse_lazy
from appMisEstacionamientos.models.contactoModels import Contacto
from appMisEstacionamientos.forms.contactoForms import ContactoForm


# irInicio()
# Vista para cargar la pagina de inicio.
def irInicio(request):
    miPlantilla = loader.get_template("inicio/index.html")
    return HttpResponse(miPlantilla.render({}, request))


# acercaDe()
# Vista para mostrar la pagina acerca de...
def acercaDe(request):
    miPlantilla = loader.get_template("inicio/acerca.html")
    return HttpResponse(miPlantilla.render({}, request))


# RegistrarMensaje:
# Vista que permite el registro de mensajes al sitio.
class RegistrarMensaje(CreateView):
    model = Contacto
    template_name = 'inicio/contactanos.html'
    form_class = ContactoForm
    success_url = reverse_lazy('mensajeRecibido')


# mensajeRecibido()
# Vista para mostrar la pagina de la recepcion del mensaje de contacto.
def mensajeRecibido(request):
    miPlantilla = loader.get_template("inicio/mensajeRecibido.html")
    return HttpResponse(miPlantilla.render({}, request))


# irBienvenida()
# Vista para cargar la pagina de bienvenida.
def irBienvenida(request):
    miPlantilla = loader.get_template("inicio/bienvenida.html")
    return HttpResponse(miPlantilla.render({}, request))
