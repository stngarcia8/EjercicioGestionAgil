from django.conf import settings
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from appMisEstacionamientos.models.tarjetasModels import Tarjeta
from appMisEstacionamientos.forms.tarjetasForm import TarjetaForm


# ListaDeTarjetas
# Clase que permite el listado de las tarjetas de pago de un usuario.
class ListaDeTarjetas(ListView):
    model = Tarjeta
    template_name = 'tarjeta/listaDeTarjetas.html'
    paginate_by = settings.REGISTROS_POR_PAGINA

    def get_queryset(self):
        result = super(ListaDeTarjetas, self).get_queryset()
        result = result.filter(usuario=self.request.user)
        query = self.request.GET.get('q')
        if query:
            result = result.filter(numero_tarjeta__contains=query)
        return result


# RegistrarTarjeta
# Clase que permite registrar una tarjeta.
class RegistrarTarjeta(CreateView):
    model = Tarjeta
    template_name = 'tarjeta/registrarTarjeta.html'
    form_class = TarjetaForm
    success_url = reverse_lazy('listaDeTarjetas')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(RegistrarTarjeta, self).form_valid(form)


# EditarTarjeta
# Clase que permite editar una tarjeta de pago.
class EditarTarjeta(UpdateView):
    model = Tarjeta
    form_class = TarjetaForm
    template_name = 'tarjeta/editarTarjeta.html'
    success_url = reverse_lazy('listaDeTarjetas')


# EliminarTarjeta
# Clase que permite eliminar una tarjeta de pago.
class EliminarTarjeta(DeleteView):
    model = Tarjeta
    template_name = 'tarjeta/eliminarTarjeta.html'
    success_url = reverse_lazy('listaDeTarjetas')


# VerTarjeta
# Clase que permite visualizar la informacion de una tarjeta de pago.
class VerTarjeta(DetailView):
    model = Tarjeta
    template_name = 'tarjeta/verTarjeta.html'
