"""# Importación de librerías propias de python
import datetime
from typing import List

# Importación de Entidades por su relacion
from Entidades.Estado import Estado
from Entidades.Llamada import Llamada
from Entidades.CategoriaLlamada import CategoriaLlamada
from Entidades.OpcionValidacion import OpcionValidacion
from Entidades.Cliente import Cliente
from Interfaces.PantallaRtaOperador import PantallaRtaOperador

# Array con los diferentes estados del objeto Estado
estados: List[Estado]  = [
    Estado("Finalizado"),
    Estado("EnCurso"),
    
]

#Datos que puede guardar el Gestor

datosLlamadas = None
estadoFinalizada: Estado = None
estadoEnCurso:Estado = None
nombreCliente = None
informacionCliente: Cliente = None
fechaActual: datetime = None
descripcionCategoriasOpcionesSubopciones = None
operador = ""
pantallaRtaOperador: PantallaRtaOperador
validaciones = None
accionRequerida = True
informacionRequerida = ""
mensajesValidacionesDeSubopcion = None


class GestorRtaOperador:
    def __init__(self, llamada: Llamada, categoriaLlamada: CategoriaLlamada):
        self.llamada = llamada
        self.categoriaLlamada = categoriaLlamada
        self.pantallaRtaOperador = PantallaRtaOperador(self)

    def nuevaRtaOperador(self):

        global datosLlamadas
        global fechaActual
        global nombreCliente
        global descripcionCategoriasOpcionesSubopciones
        global operador
        global validaciones
        global informacionCliente
        global accionRequerida
        global informacionRequerida

        self.buscarEstadoEnCurso()

        fechaActual = self.obtenerFechaHoraActual()

        self.llamada.esEnCurso(estadoEnCurso,fechaActual)

        self.obtenerDatosLlamada()

        self.pantallaRtaOperador.mostrarDatosDeLaLlamada(nombreCliente, descripcionCategoriasOpcionesSubopciones)

        self.pantallaRtaOperador.mostrarOpcionesDeValidacion(mensajesValidacionesDeSubopcion)

        self.pantallaRtaOperador.run()

    def buscarEstadoEnCurso(self):

        global estadoEnCurso

        for estado in estados:
            if estado.esEnCurso():

                estadoEnCurso = estado

    def obtenerFechaHoraActual(self):
        return datetime.datetime.now()

    def obtenerDatosLlamada(self):
        global nombreCliente
        global descripcionCategoriasOpcionesSubopciones
        global mensajesValidacionesDeSubopcion

        nombreCliente = self.llamada.getNombreClienteDeLlamada()
        descripcionCategoriasOpcionesSubopciones = self.categoriaLlamada.getDescripcionCompletaCategoriaYOpcion()
        mensajesValidacionesDeSubopcion = self.categoriaLlamada.buscarValidaciones()
        

    def tomarDatosValidacion(self, opcionSeleccionada):
        informacionCliente = self.llamada.cliente.esInformacionCorrecta(opcionSeleccionada)
        self.pantallaRegistrarRespuestaDeOperador.habilitarSeleccionRespuesta(informacionCliente, opcionSeleccionada)


    def obtenerDatosOperador(self):

        global operador

        operador = self.llamada.tomarOperador()


    def validarInformacionCliente(self):

        global informacionCliente

        informacionCliente = self.Cliente.esInformacionCorrecta()

        
    def buscarEstadoFinalizada(self):

        global estadoFinalizada

        for estado in estados:
            estadoFinalizada = estado

    def llamarCU28(self):
        global accionRequerida
        global informacionRequerida

        if accionRequerida == True:
            informacionRequerida ="Informacion Requerida exitosa"
        else:
            informacionRequerida = "Información Requerida error"   # flujo alternativo 3

    def tomarConfirmacion(self, descripcion_consulta, accion_realizar):
        global fechaHoraActualInicioLlamada
        global fechaHoraFinLlamada
        global estadoFinalizado
        self.llamarCU28(accion_realizar)
        self.buscarEstadoFinalizado()
        fechaHoraFinLlamada = self.obtenerFechaHoraActual()
        duracion = self.llamada.calcularDuracion(fechaHoraActualInicioLlamada, fechaHoraFinLlamada)
        # Seteo el estado actual de la llamada a "Finalizado"
        self.llamada.setEstadoActual(estadoFinalizado, fechaHoraFinLlamada)
        self.llamada.setDuracion(duracion)
        self.llamada.setDescripcionOperador(descripcion_consulta)
        self.pantallaRegistrarRespuestaDeOperador.mostrarMensajeDeConfirmacion()
        self.finCU()


    def finCU():
        exit()"""

import datetime
from typing import List
from Entidades.Estado import Estado
from Entidades.Llamada import Llamada
from Entidades.CategoriaLlamada import CategoriaLlamada
from Entidades.OpcionValidacion import OpcionValidacion
from Entidades.Cliente import Cliente
from Interfaces.PantallaRtaOperador import PantallaRtaOperador

estados: List[Estado] = [
    Estado("Finalizado"),
    Estado("EnCurso")
]

datosLlamadas = None
estadoFinalizada: Estado = None
estadoEnCurso: Estado = None
nombreCliente = None
informacionCliente: Cliente = None
fechaActual: datetime = None
descripcionCategoriasOpcionesSubopciones = None
operador = ""
pantallaRtaOperador: PantallaRtaOperador
validaciones = None
accionRequerida = True
informacionRequerida = ""
mensajesValidacionesDeSubopcion = None


class GestorRtaOperador:
    def __init__(self, llamada: Llamada, categoriaLlamada: CategoriaLlamada):
        self.llamada = llamada
        self.categoriaLlamada = categoriaLlamada
        self.pantallaRtaOperador = PantallaRtaOperador(self)

    def nuevaRtaOperador(self):
        global datosLlamadas
        global fechaActual
        global nombreCliente
        global descripcionCategoriasOpcionesSubopciones
        global operador
        global validaciones
        global informacionCliente
        global accionRequerida
        global informacionRequerida

        self.buscarEstadoEnCurso()

        fechaActual = self.obtenerFechaHoraActual()

        self.llamada.esEnCurso(estadoEnCurso, fechaActual)

        self.obtenerDatosLlamada()

        self.pantallaRtaOperador.mostrarDatosDeLaLlamada(nombreCliente, descripcionCategoriasOpcionesSubopciones)

        self.pantallaRtaOperador.mostrarOpcionesDeValidacion(mensajesValidacionesDeSubopcion)

        self.pantallaRtaOperador.run()

    def buscarEstadoEnCurso(self):
        global estadoEnCurso
        for estado in estados:
            if estado.esEnCurso():
                estadoEnCurso = estado

    def obtenerFechaHoraActual(self):
        return datetime.datetime.now()

    def obtenerDatosLlamada(self):
        global nombreCliente
        global descripcionCategoriasOpcionesSubopciones
        global mensajesValidacionesDeSubopcion
        nombreCliente = self.llamada.getNombreClienteDeLlamada()
        descripcionCategoriasOpcionesSubopciones = self.categoriaLlamada.getDescripcionCompletaCategoriaYOpcion()
        mensajesValidacionesDeSubopcion = self.categoriaLlamada.buscarValidaciones()

    def tomarOpcionDeValidacion(self, opcionSeleccionada):
        informacionCliente = self.llamada.cliente.esInformacionCorrecta(opcionSeleccionada)
        self.pantallaRtaOperador.habilitarSeleccionRespuesta(informacionCliente, opcionSeleccionada)

    def obtenerDatosOperador(self):
        global operador
        operador = self.llamada.tomarOperador()

    def validarInformacionCliente(self):
        global informacionCliente
        informacionCliente = self.Cliente.esInformacionCorrecta()

    def buscarEstadoFinalizada(self):
        global estadoFinalizada
        for estado in estados:
            estadoFinalizada = estado

    def llamarCU28(self, accion_requerida):
        global accionRequerida
        global informacionRequerida
        if accion_requerida:
            informacionRequerida = "Informacion Requerida exitosa"
        else:
            informacionRequerida = "Información Requerida error"  # flujo alternativo 3

    def tomarConfirmacion(self, descripcion_consulta, accion_realizar):
        global fechaHoraActualInicioLlamada
        global fechaHoraFinLlamada
        global estadoFinalizado
        self.llamarCU28(accion_realizar)
        self.buscarEstadoFinalizada()
        fechaHoraFinLlamada = self.obtenerFechaHoraActual()
        duracion = self.llamada.calcularDuracion(fechaHoraActualInicioLlamada, fechaHoraFinLlamada)
        self.llamada.setEstadoActual(estadoFinalizado, fechaHoraFinLlamada)
        self.llamada.setDuracion(duracion)
        self.llamada.setDescripcionOperador(descripcion_consulta)
        self.pantallaRtaOperador.mostrarMensajeDeConfirmacion()
        self.finCU()

    def finCU(self):
        exit()