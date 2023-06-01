# Importación de librerías propias de python
import datetime
from typing import List

# Importación de Entidades por su relacion
from Entidades.Estado import Estado
from Entidades.Llamada import Llamada
from Entidades.CategoriaLlamada import CategoriaLlamada
from Entidades import OpcionValidacion
from Entidades.Cliente import Cliente
from Interfaces.PantallaRtaOperador import PantallaRtaOperador

# Array con los diferentes estados del objeto Estado
estados: List[Estado]  = [
    Estado("Finalizado"),
    Estado("Iniciado")
]

#Datos que puede guardar el Gestor

datosLlamadas = None
estadoFinalizada: Estado = None
estadoEnCurso:Estado = None
nombreCliente = None
fechaActual: datetime = None
descripcionCategoriasOpcionesSubopciones = None
operador = ""
pantallaRtaOperador: PantallaRtaOperador
validaciones = None


class GestorRtaOperador:
    def __init__(self, llamada: Llamada, categoriaLlamada: CategoriaLlamada):
        self.llamada = llamada
        self.categoriaLlamada = categoriaLlamada
        self.pantallaRtaOperador = PantallaRtaOperador(self)

    def nuevaRtaOperador(self):

        global datosLlamadas
        global estadoEnCurso
        global estadoFinalizada
        global fechaActual
        global nombreCliente
        global descripcionCategoriasOpcionesSubopciones
        global operador
        global validaciones

        self.buscarEstadoEnCurso()

        fechaActual = self.obtenerFechaActual()

        self.llamada.setEstadoActual(estadoEnCurso,fechaActual)

        self.obtenerDatosLlamada()

        self.pantallaRtaOperador.mostrarDatosLlamada(nombreCliente, descripcionCategoriasOpcionesSubopciones)

        self.pantallaRtaOperador.mostrarValidaciones(validaciones)

        self.pantallaRtaOperador.run()

        def buscarEstadoEnCurso(self):

            global estadoEnCurso

            for estado in estados:
                estadoEnCurso = estado

        def obtenerFechaActual(self):
            return datetime.now()

        def obtenerDatosLlamada(self):
            global nombreCliente
            global descripcionCategoriasOpcionesSubopciones
            global validaciones

            nombreCliente = self.llamada.getNombreClienteDeLlamada()
            validaciones = self.validacion.getMensajeValidacion()

        def buscarValidaciones(self):
            global validaciones

            validaciones = self.opcionValidacion.getCorrecta()


        

        
