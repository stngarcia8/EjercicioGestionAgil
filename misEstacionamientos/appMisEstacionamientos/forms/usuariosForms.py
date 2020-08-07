from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from appMisEstacionamientos.models.personaModels import Persona


# UsuarioCreateForm
# Formulario de registro de usuarios.
class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


# UsuarioEditCredencialesForm
# Formulario para cambiar credenciales de usuario.
class UsuarioEditCredencialesForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


# UsuarioForm:
# Formulario para datos personales del usuario registrado.
class UsuarioForm(ModelForm):
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'rut',
                  'email', 'nacimiento', 'telefono')
