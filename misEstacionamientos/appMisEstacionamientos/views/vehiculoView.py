from django.conf import settings
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from appMisEstacionamientos.models.vehiculoModels import Vehiculo
from appMisEstacionamientos.forms.vehiculoForm import VehiculoForm


# ListaDeVehiculos
# Clase que permite el listado de los vehiculos de un usuario.
class ListaDeVehiculos(ListView):
    model = Vehiculo
    template_name = 'vehiculos/listaDeVehiculos.html'
    paginate_by = settings.REGISTROS_POR_PAGINA

    def get_queryset(self):
        result = super(ListaDeVehiculos, self).get_queryset()
        result = result.filter(usuario=self.request.user)
        query = self.request.GET.get('q')
        if query:
            result = result.filter(patente__contains=query)
        return result


# RegistrarVehiculo
# Clase que permite registrar una nueva sucursal.
class RegistrarVehiculo(CreateView):
    model = Vehiculo
    template_name = 'vehiculos/registrarVehiculo.html'
    form_class = VehiculoForm
    success_url = reverse_lazy('listaDeVehiculos')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(RegistrarVehiculo, self).form_valid(form)


# EditarVehiculo
# Clase que permite editar la informacion de un vehiculo.
class EditarVehiculo(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculos/editarVehiculo.html'
    success_url = reverse_lazy('listaDeVehiculos')


# EliminarVehiculo
# Clase que permite eliminar un vehiculo.
class EliminarVehiculo(DeleteView):
    model = Vehiculo
    template_name = 'vehiculos/eliminarVehiculo.html'
    success_url = reverse_lazy('listaDeVehiculos')


# VerVehiculo
# Clase que permite visualizar la informacion de un vehiculo.
class VerVehiculo(DetailView):
    model = Vehiculo
    template_name = 'vehiculos/verVehiculo.html'
