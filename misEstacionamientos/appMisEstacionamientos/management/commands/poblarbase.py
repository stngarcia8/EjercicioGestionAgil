from appMisEstacionamientos.models.helperModels import Color, Marca
from appMisEstacionamientos.models.helperModels import TipoDireccion, TipoVivienda, Comuna
from appMisEstacionamientos.models.helperModels import Banco, TipoTarjeta
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Ingresa valores de prueba para MisEstacionamientos.'

    def handle(self, *args, **kwargs):
        self.crearColores()
        self.crearMarcas()
        self.crearTipoDireccion()
        self.crearTipoVivienda()
        self.crearComunas()
        self.crearTipoTarjeta()
        self.crearBancos()
        print('Base de datos poblada para pruebas!')

    # crearColores()
    # Metodo para crear colores de ejemplo.
    def crearColores(self):
        print('Creando colores...')
        myColor = Color(nombre='Blanco ', nombre_web='White ')
        myColor.save()
        myColor = Color(nombre='Negro ', nombre_web='Black ')
        myColor.save()
        myColor = Color(nombre='Gris Claro ', nombre_web='LightGrey ')
        myColor.save()
        myColor = Color(nombre='Gris Plata ', nombre_web='Silver ')
        myColor.save()
        myColor = Color(nombre='Gris Oscuro ', nombre_web='DarkGray ')
        myColor.save()
        myColor = Color(nombre='Gris ', nombre_web='Gray ')
        myColor.save()
        myColor = Color(nombre='Rojo Puro ', nombre_web='Red ')
        myColor.save()
        myColor = Color(nombre='Rojo Fuego ', nombre_web='FireBrick ')
        myColor.save()
        myColor = Color(nombre='Rojo Oscuro ', nombre_web='DarkRed ')
        myColor.save()
        myColor = Color(nombre='Rosa ', nombre_web='Pink ')
        myColor.save()
        myColor = Color(nombre='Rosa Suave ', nombre_web='LightPink ')
        myColor.save()
        myColor = Color(nombre='Rosa Cálido ', nombre_web='HotPink ')
        myColor.save()
        myColor = Color(nombre='Naranja Rojizo ', nombre_web='OrangeRed ')
        myColor.save()
        myColor = Color(nombre='Naranja Oscuro ', nombre_web='DarkOrange ')
        myColor.save()
        myColor = Color(nombre='Naranja Puro ', nombre_web='Orange ')
        myColor.save()
        myColor = Color(nombre='Amarillo Puro ', nombre_web='Yellow ')
        myColor.save()
        myColor = Color(nombre='Amarillo Suave ', nombre_web='LightYellow ')
        myColor.save()
        myColor = Color(nombre='Violeta ', nombre_web='Violet ')
        myColor.save()
        myColor = Color(nombre='Medio Violeta Rojo ', nombre_web='MediumVioletRed ')
        myColor.save()
        myColor = Color(nombre='Violeta Oscuro ', nombre_web='DarkViolet ')
        myColor.save()
        myColor = Color(nombre='Magenta ', nombre_web='Magenta ')
        myColor.save()
        myColor = Color(nombre='Magenta Oscuro ', nombre_web='DarkMagenta ')
        myColor.save()
        myColor = Color(nombre='Púrpura ', nombre_web='Purple ')
        myColor.save()
        myColor = Color(nombre='Púrpura Medio ', nombre_web='MediumPurple ')
        myColor.save()
        myColor = Color(nombre='Verde Claro ', nombre_web='LightGreen ')
        myColor.save()
        myColor = Color(nombre='Verde ', nombre_web='Green ')
        myColor.save()
        myColor = Color(nombre='Verde Oscuro ', nombre_web='DarkGreen ')
        myColor.save()
        myColor = Color(nombre='Cyan ', nombre_web='Cyan ')
        myColor.save()
        myColor = Color(nombre='Cyan Suave ', nombre_web='LightCyan ')
        myColor.save()
        myColor = Color(nombre='Cyan Oscuro ', nombre_web='DarkCyan ')
        myColor.save()
        myColor = Color(nombre='Turquesa ', nombre_web='Turquoise ')
        myColor.save()
        myColor = Color(nombre='Turquesa Medio ', nombre_web='MediumTurquoise ')
        myColor.save()
        myColor = Color(nombre='Turquesa Oscuro ', nombre_web='DarkTurquoise ')
        myColor.save()
        myColor = Color(nombre='Azul ', nombre_web='Blue ')
        myColor.save()
        myColor = Color(nombre='Azul Medio ', nombre_web='MediumBlue ')
        myColor.save()
        myColor = Color(nombre='Azul Oscuro ', nombre_web='DarkBlue ')
        myColor.save()

    # crearMarcas()
    # Metodo para crear marcas de ejemplo.
    def crearMarcas(self):

        print('Creando marcas...')
        myMarca = Marca(nombre='ALFA ROMEO')
        myMarca.save()
        myMarca = Marca(nombre='ASIA MOTORS')
        myMarca.save()
        myMarca = Marca(nombre='ASTON MARTIN')
        myMarca.save()
        myMarca = Marca(nombre='AUDI')
        myMarca.save()
        myMarca = Marca(nombre='AUSTIN')
        myMarca.save()
        myMarca = Marca(nombre='AUTORRAD')
        myMarca.save()
        myMarca = Marca(nombre='BAIC')
        myMarca.save()
        myMarca = Marca(nombre='BMW')
        myMarca.save()
        myMarca = Marca(nombre='BRILLIANCE')
        myMarca.save()
        myMarca = Marca(nombre='BYD')
        myMarca.save()
        myMarca = Marca(nombre='CADILLAC')
        myMarca.save()
        myMarca = Marca(nombre='CHANGAN')
        myMarca.save()
        myMarca = Marca(nombre='CHANGHE')
        myMarca.save()
        myMarca = Marca(nombre='CHERY')
        myMarca.save()
        myMarca = Marca(nombre='CHEVROLET')
        myMarca.save()
        myMarca = Marca(nombre='CHRYSLER')
        myMarca.save()
        myMarca = Marca(nombre='CITROËN')
        myMarca.save()
        myMarca = Marca(nombre='DAEWOO')
        myMarca.save()
        myMarca = Marca(nombre='DAIHATSU')
        myMarca.save()
        myMarca = Marca(nombre='DATSUN')
        myMarca.save()
        myMarca = Marca(nombre='DFM')
        myMarca.save()
        myMarca = Marca(nombre='DFSK')
        myMarca.save()
        myMarca = Marca(nombre='DODGE')
        myMarca.save()
        myMarca = Marca(nombre='DONGFENG')
        myMarca.save()
        myMarca = Marca(nombre='FAW')
        myMarca.save()
        myMarca = Marca(nombre='FERRARI')
        myMarca.save()
        myMarca = Marca(nombre='FIAT')
        myMarca.save()
        myMarca = Marca(nombre='FORD')
        myMarca.save()
        myMarca = Marca(nombre='FOTON')
        myMarca.save()
        myMarca = Marca(nombre='GAC GONOW')
        myMarca.save()
        myMarca = Marca(nombre='GEELY')
        myMarca.save()
        myMarca = Marca(nombre='GMC')
        myMarca.save()
        myMarca = Marca(nombre='GREAT WALL')
        myMarca.save()
        myMarca = Marca(nombre='HAFEI')
        myMarca.save()
        myMarca = Marca(nombre='HAIMA')
        myMarca.save()
        myMarca = Marca(nombre='HONDA')
        myMarca.save()
        myMarca = Marca(nombre='HUMMER')
        myMarca.save()
        myMarca = Marca(nombre='HYUNDAI')
        myMarca.save()
        myMarca = Marca(nombre='INFINITI')
        myMarca.save()
        myMarca = Marca(nombre='ISUZU')
        myMarca.save()
        myMarca = Marca(nombre='IVECO')
        myMarca.save()
        myMarca = Marca(nombre='JAC')
        myMarca.save()
        myMarca = Marca(nombre='JAGUAR')
        myMarca.save()
        myMarca = Marca(nombre='JEEP')
        myMarca.save()
        myMarca = Marca(nombre='JINBEI')
        myMarca.save()
        myMarca = Marca(nombre='JMC')
        myMarca.save()
        myMarca = Marca(nombre='KIA')
        myMarca.save()
        myMarca = Marca(nombre='LADA')
        myMarca.save()
        myMarca = Marca(nombre='LAMBORGHINI')
        myMarca.save()
        myMarca = Marca(nombre='LAND ROVER')
        myMarca.save()
        myMarca = Marca(nombre='LEXUS')
        myMarca.save()
        myMarca = Marca(nombre='LIFAN')
        myMarca.save()
        myMarca = Marca(nombre='MAHINDRA')
        myMarca.save()
        myMarca = Marca(nombre='MASERATI')
        myMarca.save()
        myMarca = Marca(nombre='MAXUS')
        myMarca.save()
        myMarca = Marca(nombre='MAZDA')
        myMarca.save()
        myMarca = Marca(nombre='MCLAREN')
        myMarca.save()
        myMarca = Marca(nombre='MERCEDES BENZ')
        myMarca.save()
        myMarca = Marca(nombre='MG')
        myMarca.save()
        myMarca = Marca(nombre='MINI')
        myMarca.save()
        myMarca = Marca(nombre='MITSUBISHI MOTORS')
        myMarca.save()
        myMarca = Marca(nombre='NISSAN')
        myMarca.save()
        myMarca = Marca(nombre='OLDSMOBILE')
        myMarca.save()
        myMarca = Marca(nombre='OPEL')
        myMarca.save()
        myMarca = Marca(nombre='PEUGEOT')
        myMarca.save()
        myMarca = Marca(nombre='PIAGGIO')
        myMarca.save()
        myMarca = Marca(nombre='PONTIAC')
        myMarca.save()
        myMarca = Marca(nombre='PORSCHE')
        myMarca.save()
        myMarca = Marca(nombre='PROTON')
        myMarca.save()
        myMarca = Marca(nombre='RENAULT')
        myMarca.save()
        myMarca = Marca(nombre='RENAULT SAMSUNG')
        myMarca.save()
        myMarca = Marca(nombre='ROLLS ROYCE')
        myMarca.save()
        myMarca = Marca(nombre='ROVER')
        myMarca.save()
        myMarca = Marca(nombre='SAAB')
        myMarca.save()
        myMarca = Marca(nombre='SEAT')
        myMarca.save()
        myMarca = Marca(nombre='SKODA')
        myMarca.save()
        myMarca = Marca(nombre='SSANGYONG')
        myMarca.save()
        myMarca = Marca(nombre='SUBARU')
        myMarca.save()
        myMarca = Marca(nombre='SUZUKI')
        myMarca.save()
        myMarca = Marca(nombre='TOYOTA')
        myMarca.save()
        myMarca = Marca(nombre='TRIUMPH')
        myMarca.save()
        myMarca = Marca(nombre='VOLKSWAGEN')
        myMarca.save()
        myMarca = Marca(nombre='VOLVO')
        myMarca.save()
        myMarca = Marca(nombre='ZASTAVA')
        myMarca.save()
        myMarca = Marca(nombre='ZNA')
        myMarca.save()
        myMarca = Marca(nombre='ZOTYE')
        myMarca.save()

    # crearTipoDireccion()
    # Metodo para crear tipos de direcciones.
    def crearTipoDireccion(self):
        print('Creando tipos de direcciones...')
        miTipo = TipoDireccion(nombre='Avenida')
        miTipo.save()
        miTipo = TipoDireccion(nombre='Calle')
        miTipo.save()
        miTipo = TipoDireccion(nombre='Pasaje')
        miTipo.save()

    # crearTipoVivienda()
    # Metodo para crear tipos de viviendas.
    def crearTipoVivienda(self):
        print('Creando tipos de viviendas...')
        miTipo = TipoVivienda(nombre='Casa')
        miTipo.save()
        miTipo = TipoVivienda(nombre='Departamento')
        miTipo.save()

    # crearComunas()
    # Metodo para crear comunas de prueba.
    def crearComunas(self):
        print('Creando comunas...')
        miComuna = Comuna(nombre='Cerrillos')
        miComuna.save()
        miComuna = Comuna(nombre='La Reina')
        miComuna.save()
        miComuna = Comuna(nombre='Pudahuel')
        miComuna.save()
        miComuna = Comuna(nombre='Cerro Navia')
        miComuna.save()
        miComuna = Comuna(nombre='Las Condes')
        miComuna.save()
        miComuna = Comuna(nombre='Quilicura')
        miComuna.save()
        miComuna = Comuna(nombre='Conchalí')
        miComuna.save()
        miComuna = Comuna(nombre='Lo Barnechea')
        miComuna.save()
        miComuna = Comuna(nombre='Quinta Normal')
        miComuna.save()
        miComuna = Comuna(nombre='El Bosque')
        miComuna.save()
        miComuna = Comuna(nombre='Lo Espejo')
        miComuna.save()
        miComuna = Comuna(nombre='Recoleta')
        miComuna.save()
        miComuna = Comuna(nombre='Estación Central')
        miComuna.save()
        miComuna = Comuna(nombre='Lo Prado')
        miComuna.save()
        miComuna = Comuna(nombre='Renca')
        miComuna.save()
        miComuna = Comuna(nombre='Huechuraba')
        miComuna.save()
        miComuna = Comuna(nombre='Macul')
        miComuna.save()
        miComuna = Comuna(nombre='San Joaquín')
        miComuna.save()
        miComuna = Comuna(nombre='Independencia')
        miComuna.save()
        miComuna = Comuna(nombre='Maipú')
        miComuna.save()
        miComuna = Comuna(nombre='San Miguel')
        miComuna.save()
        miComuna = Comuna(nombre='La Cisterna')
        miComuna.save()
        miComuna = Comuna(nombre='Ñunoa')
        miComuna.save()
        miComuna = Comuna(nombre='San Ramón')
        miComuna.save()
        miComuna = Comuna(nombre='La Florida')
        miComuna.save()
        miComuna = Comuna(nombre='Pedro Aguirre Cerda')
        miComuna.save()
        miComuna = Comuna(nombre='Santiago')
        miComuna.save()
        miComuna = Comuna(nombre='La Granja')
        miComuna.save()
        miComuna = Comuna(nombre='Peñalolén')
        miComuna.save()
        miComuna = Comuna(nombre='Vitacura')
        miComuna.save()
        miComuna = Comuna(nombre='La Pintana')
        miComuna.save()
        miComuna = Comuna(nombre='Providencia')
        miComuna.save()
        miComuna = Comuna(nombre='Padre Hurtado')
        miComuna.save()
        miComuna = Comuna(nombre='San Bernardo')
        miComuna.save()
        miComuna = Comuna(nombre='Puente Alto')
        miComuna.save()
        miComuna = Comuna(nombre='Pirque')
        miComuna.save()
        miComuna = Comuna(nombre='San José de Maipo')
        miComuna.save()

    # crearTipoTarjeta()
    # Metodo para crear un tipo de tarjeta.
    def crearTipoTarjeta(self):
        print('Creando tipo de tarjeta...')
        miTarjeta = TipoTarjeta(nombre='Visa')
        miTarjeta.save()
        miTarjeta = TipoTarjeta(nombre='Master card')
        miTarjeta.save()
        miTarjeta = TipoTarjeta(nombre='Debito')
        miTarjeta.save()

    # crearBancos()
    # Metodo para crear bancos de prueba.
    def crearBancos(self):
        print('Creando bancos...')
        miBanco = Banco(nombre='Banco Bci')
        miBanco.save()
        miBanco = Banco(nombre='Banco de Chile')
        miBanco.save()
        miBanco = Banco(nombre='Banco Estado')
        miBanco.save()
        miBanco = Banco(nombre='Banco Santander')
        miBanco.save()
        miBanco = Banco(nombre='Banco BICE')
        miBanco.save()
        miBanco = Banco(nombre='Banco Condell')
        miBanco.save()
        miBanco = Banco(nombre='Banco CrediChile')
        miBanco.save()
        miBanco = Banco(nombre='Banco Edwards Citi')
        miBanco.save()
        miBanco = Banco(nombre='Banco Falabella')
        miBanco.save()
        miBanco = Banco(nombre='Banco Internacional')
        miBanco.save()
        miBanco = Banco(nombre='Banco Itaú')
        miBanco.save()
        miBanco = Banco(nombre='Banco Ripley')
        miBanco.save()
        miBanco = Banco(nombre='Banco Security')
        miBanco.save()
        miBanco = Banco(nombre='CorpBanca')
        miBanco.save()
        miBanco = Banco(nombre='Santander Banefe')
        miBanco.save()
        miBanco = Banco(nombre='Scotiabank')
        miBanco.save()
        miBanco = Banco(nombre='Scotiabank Azul (ex BBVA)')
        miBanco.save()
