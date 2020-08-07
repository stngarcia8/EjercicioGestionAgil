from django.conf import settings
from geopy.geocoders import Nominatim
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from appMisEstacionamientos.models.direccionModels import Direccion
from appMisEstacionamientos.forms.direccionForm import DireccionForm


# ListaDeDirecciones
# Clase que permite el listado de las direcciones de un usuario.
class ListaDeDirecciones(ListView):
    model = Direccion
    template_name = 'direccion/listaDeDirecciones.html'
    paginate_by = settings.REGISTROS_POR_PAGINA

    def get_queryset(self):
        result = super(ListaDeDirecciones, self).get_queryset()
        result = result.filter(usuario=self.request.user)
        query = self.request.GET.get('q')
        if query:
            result = result.filter(direccion__contains=query)
        return result


# RegistrarDireccion
# Clase que permite registrar una direccion.
class RegistrarDireccion(CreateView):
    model = Direccion
    template_name = 'direccion/registrarDireccion.html'
    form_class = DireccionForm
    success_url = reverse_lazy('listaDeDirecciones')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.get_localizacion((self.object))
        self.object.save()
        return super(RegistrarDireccion, self).form_valid(form)

    def get_localizacion(self, dir):
        direccion = dir.tipo_direccion.nombre + ' ' + dir.direccion + ', ' + dir.numero + ', ' + dir.comuna.nombre
        try:
            geoLocalizador = Nominatim(user_agent="misEstacionamientos")
            localizacion = geoLocalizador.geocode(direccion)
            dir.direccionLocator = localizacion.address
            dir.longitudLocator = localizacion.longitude
            dir.latitudLocator = localizacion.latitude
        except ValueError:
            dir.direccionLocator = None
            dir.longitudLocator = 0
            dir.latitudLocator = 0


# EditarDireccion
# Clase que permite editar una direccion.
class EditarDireccion(UpdateView):
    model = Direccion
    form_class = DireccionForm
    template_name = 'direccion/editarDireccion.html'
    success_url = reverse_lazy('listaDeDirecciones')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.get_localizacion((self.object))
        self.object.save()
        return super(RegistrarDireccion, self).form_valid(form)

    def get_localizacion(self, dir):
        direccion = dir.tipo_direccion.nombre + ' ' + dir.direccion + ', ' + dir.numero + ', Santiago'
        try:
            geoLocalizador = Nominatim(user_agent="misEstacionamientos")
            localizacion = geoLocalizador.geocode(direccion)
            dir.direccionLocator = localizacion.address
            dir.longitudLocator = localizacion.longitude
            dir.latitudLocator = localizacion.latitude
        except ValueError:
            dir.direccionLocator = None
            dir.longitudLocator = 0
            dir.latitudLocator = 0


# EliminarDireccion
# Clase que permite eliminar una direccion.
class EliminarDireccion(DeleteView):
    model = Direccion
    template_name = 'direccion/eliminarDireccion.html'
    success_url = reverse_lazy('listaDeDirecciones')


# VerDireccion
# Clase que permite visualizar la informacion de una direccion.
class VerDireccion(DetailView):
    model = Direccion
    template_name = 'direccion/verDireccion.html'
