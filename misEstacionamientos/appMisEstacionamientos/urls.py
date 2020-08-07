from django.conf.urls import url
from appMisEstacionamientos.views import inicioView, usuarioView, loginView, vehiculoView, direccionView, tarjetaView
from appMisEstacionamientos.views import estacionamientosView


urlpatterns = [
    # rutas de la pantalla de inicio.
    url(r'^$', inicioView.irInicio, name='irInicio'),
    url(r'^acerca/$', inicioView.acercaDe, name='acercaDe'),
    url(r'^registrar/contacto/$', inicioView.RegistrarMensaje.as_view(),
        name='registrarMensaje'),
    url(r'^mensajeRecibido/$', inicioView.mensajeRecibido, name='mensajeRecibido'),
    url(r'^bienvenida/$', inicioView.irBienvenida, name='irBienvenida'),


    # Rutas del manejo de la sesion.
    url(r'^login/iniciarSesion/$', loginView.iniciarSesion, name='iniciarSesion'),
    url(r'^login/cerrarSesion/$', loginView.cerrarSesion, name='cerrarSesion'),
    url(r'^login/denegarAcceso/$', loginView.denegarAcceso, name='denegarAcceso'),
    url(r'^login/restringirAcceso/$',
        loginView.restringirAcceso, name='restringirAcceso'),

    # Rutas para el registro de usuario y mantenimiento del perfil.
    url(r'^registrar/usuario/$', usuarioView.RegistrarUsuario.as_view(),
        name='registrarUsuario'),
    url(r'^ver/usuario/(?P<pk>\d+)$',
        usuarioView.VerUsuario.as_view(), name='verUsuario'),
    url(r'^editar/usuario/(?P<pk>\d+)$',
        usuarioView.EditarUsuario.as_view(), name='editarUsuario'),
    url(r'^eliminar/usuario/(?P<pk>\d+)$',
        usuarioView.EliminarUsuario.as_view(), name='eliminarUsuario'),
    url(r'^editar/usuario/credenciales/(?P<pk>\d+)$',
        usuarioView.EditarCredencialesUsuario.as_view(), name='editarCredencialesUsuario'),

    # Rutas de los vehiculos.
    url(r'^lista/vehiculo/$', vehiculoView.ListaDeVehiculos.as_view(),
        name='listaDeVehiculos'),
    url(r'^registrar/vehiculo/$', vehiculoView.RegistrarVehiculo.as_view(),
        name='registrarVehiculo'),
    url(r'^editar/vehiculo/(?P<pk>\d+)$',
        vehiculoView.EditarVehiculo.as_view(), name='editarVehiculo'),
    url(r'^eliminar/vehiculo/(?P<pk>\d+)$',
        vehiculoView.EliminarVehiculo.as_view(), name='eliminarVehiculo'),
    url(r'^ver/vehiculo/(?P<pk>\d+)$',
        vehiculoView.VerVehiculo.as_view(), name='verVehiculo'),

    # Rutas de las direcciones.
    url(r'^lista/direccion/$', direccionView.ListaDeDirecciones.as_view(),
        name='listaDeDirecciones'),
    url(r'^registrar/direccion/$', direccionView.RegistrarDireccion.as_view(),
        name='registrarDireccion'),
    url(r'^editar/direccion/(?P<pk>\d+)$',
        direccionView.EditarDireccion.as_view(), name='editarDireccion'),
    url(r'^eliminar/direccion/(?P<pk>\d+)$',
        direccionView.EliminarDireccion.as_view(), name='eliminarDireccion'),
    url(r'^ver/direccion/(?P<pk>\d+)$',
        direccionView.VerDireccion.as_view(), name='verDireccion'),

    # Rutas de las tarjetas de pago..
    url(r'^lista/tarjeta/$', tarjetaView.ListaDeTarjetas.as_view(),
        name='listaDeTarjetas'),
    url(r'^registrar/tarjeta/$', tarjetaView.RegistrarTarjeta.as_view(),
        name='registrarTarjeta'),
    url(r'^editar/tarjeta/(?P<pk>\d+)$',
        tarjetaView.EditarTarjeta.as_view(), name='editarTarjeta'),
    url(r'^eliminar/tarjeta/(?P<pk>\d+)$',
        tarjetaView.EliminarTarjeta.as_view(), name='eliminarTarjeta'),
    url(r'^ver/tarjeta/(?P<pk>\d+)$',
        tarjetaView.VerTarjeta.as_view(), name='verTarjeta'),

    # Rutas de estacionamientos
    url(r'^lista/estacionamiento/$', estacionamientosView.ListaEstacionamientos.as_view(),
        name='listaEstacionamientos'),
    url(r'^registrar/estacionamiento/$', estacionamientosView.RegistrarEstacionamiento.as_view(),
        name='RegistrarEstacionamiento'),
    url(r'^editar/estacionamiento/(?P<pk>\d+)$',
        estacionamientosView.EditarEstacionamiento.as_view(), name='editarEstacionamiento'),
    url(r'^eliminar/estacionamiento/(?P<pk>\d+)$',
        estacionamientosView.EliminarEstacionamiento.as_view(), name='eliminarEstacionamiento'),
    url(r'^ver/estacionamiento/(?P<pk>\d+)$',
        estacionamientosView.VerEstacionamiento.as_view(), name='verEstacionamiento'),

    # Rutas de las acciones de los estacionamientos.
    url(r'^lista/estacionamiento/disponibles/$', estacionamientosView.ListaEstacionamientosDisponibles.as_view(),
        name='listaEstacionamientosDisponibles'),
    url(r'^habilitar/estacionamiento/(?P<pk>\d+)$',
        estacionamientosView.habilitarEstacionamiento, name='habilitarEstacionamiento'),
    url(r'^inhabilitar/estacionamiento/(?P<pk>\d+)$',
        estacionamientosView.inhabilitarEstacionamiento, name='inhabilitarEstacionamiento'),
]
