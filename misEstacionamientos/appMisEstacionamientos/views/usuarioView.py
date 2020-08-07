from django.views.generic import CreateView,  UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from appMisEstacionamientos.forms.usuariosForms import UsuarioForm, UsuarioEditCredencialesForm
from appMisEstacionamientos.models.personaModels import Persona


# RegistrarUsuario
# Clase que permite registrar un nuevo usuario.
class RegistrarUsuario(CreateView):
    model = Persona
    form_class = UsuarioForm
    template_name = 'usuarios/registrarUsuario.html'
    success_url = reverse_lazy('irBienvenida')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        data = form.cleaned_data
        miUsuario = User.objects.create_user(
            username=data.get('rut'),
            email=data.get('email'),
            password=data.get('rut'),
            first_name=data.get('nombre'),
            last_name=data.get('apellido'),
            is_staff=False,
            is_superuser=False)
        miUsuario.save()
        self.object.usuario = miUsuario
        self.object.save
        return super(RegistrarUsuario, self).form_valid(form)


# VerPerfil:
# Clase que muestra el perfil del usuario.
class VerUsuario(DetailView):
    model = Persona
    template_name = 'usuarios/verUsuario.html'


# EditarUsuario
# Clase que permite editar los datos personales de un usuario.
class EditarUsuario(UpdateView):
    model = Persona
    form_class = UsuarioForm
    template_name = 'usuarios/editarUsuario.html'
    success_url = reverse_lazy('irInicio')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        data = form.cleaned_data
        self.request.user.first_name = data.get('nombre')
        self.request.user.last_name = data.get('apellido')
        self.request.user.email = data.get('email')
        self.request.user.save
        self.object.save
        return super(EditarUsuario, self).form_valid(form)


# EliminarUsuario
# Clase que permite eliminar un usuario.
class EliminarUsuario(DeleteView):
    login_required = True
    model = User
    template_name = 'usuarios/eliminarUsuario.html'
    success_url = reverse_lazy('irInicio')


# EditarCredencialesUsuario
# Clase que permite editar las credenciales del usuario registrado.
class EditarCredencialesUsuario(UpdateView):
    login_required = True
    model = User
    form_class = UsuarioEditCredencialesForm
    template_name = 'usuarios/editarCredencialesUsuario.html'
    success_url = reverse_lazy('iniciarSesion')
