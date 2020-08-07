from django.views.generic import CreateView,  UpdateView, DeleteView, DetailView, ListView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse_lazy
from appMisEstacionamientos.forms.estacionamientoForms import EstacionamientosForm
from appMisEstacionamientos.models.estacionamientoModels import Estacionamiento


# Nombre descriptivo Estacionamientos
# Clase que registra un estacionamiento.
class RegistrarEstacionamiento(CreateView):
    model = Estacionamiento
    form_class = EstacionamientosForm
    template_name = 'estacionamiento/registrarEstacionamiento.html'
    success_url = reverse_lazy('listaEstacionamientos')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print(self.request.user)
        self.object.usuario = self.request.user
        print(self.object.usuario)
        self.object.save
        return super(RegistrarEstacionamiento, self).form_valid(form)


# ListaEstacionamientos
# Clase que permite el listado de los Estacionamientos.
class ListaEstacionamientos(ListView):
    model = Estacionamiento
    template_name = 'estacionamiento/listarEstacionamientos.html'
    paginate_by = settings.REGISTROS_POR_PAGINA

    def get_queryset(self):
        result = super(ListaEstacionamientos, self).get_queryset()
        result = result.filter(usuario=self.request.user)
        query = self.request.GET.get('q')
        if query:
            result = result.filter(nombreDescriptivo__contains=query)
        return result


# EditarEstacionamiento
# Clase que permite editar un estacionamiento.
class EditarEstacionamiento(UpdateView):
    model = Estacionamiento
    form_class = EstacionamientosForm
    template_name = 'estacionamiento/editarEstacionamiento.html'
    success_url = reverse_lazy('listaEstacionamientos')


# EliminarEstacionamiento
# Clase que permite eliminar un estacionamiento.
class EliminarEstacionamiento(DeleteView):
    model = Estacionamiento
    template_name = 'estacionamiento/eliminarEstacionamiento.html'
    success_url = reverse_lazy('listaEstacionamientos')


# VerEstacionamiento:
# Clase que muestra un Estacionamiento.
class VerEstacionamiento(DetailView):
    model = Estacionamiento
    template_name = 'estacionamiento/verEstacionamiento.html'


# ListaEstacionamientosDisponibles
# Clase que permite el listado de los Estacionamientos disponibles.
class ListaEstacionamientosDisponibles(ListView):
    model = Estacionamiento
    template_name = 'estacionamiento/listarEstacionamientosDisponibles.html'
    paginate_by = settings.REGISTROS_POR_PAGINA

    def get_queryset(self):
        result = super(ListaEstacionamientosDisponibles, self).get_queryset()
        result = result.filter(disponibilidadEstacionamiento=True)
        query = self.request.GET.get('q')
        if query:
            result = result.filter(nombreDescriptivo__contains=query)
        return result


# Habilitar estacionamiento
# Vista que permite la habilitacion del estacionamiento para su arriendo.
@login_required(login_url='iniciarSesion')
def habilitarEstacionamiento(request, pk):
    miEstacionamiento = Estacionamiento.objects.get(id=pk)
    miEstacionamiento.disponibilidadEstacionamiento = True
    miEstacionamiento.save()
    return redirect('listaEstacionamientos')


# inhabilitar estacionamiento
# Vista que permite la inhabilitacion del estacionamiento para su arriendo.
@login_required(login_url='iniciarSesion')
def inhabilitarEstacionamiento(request, pk):
    miEstacionamiento = Estacionamiento.objects.get(id=pk)
    miEstacionamiento.disponibilidadEstacionamiento = False
    miEstacionamiento.save()
    return redirect('listaEstacionamientos')
