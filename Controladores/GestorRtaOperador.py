# Importación de python
import datetime
from typing import List

# Importación de Entidades
from Entidades.Estado import Estado
from Entidades.Llamada import Llamada
from Entidades.CategoriaLlamada import CategoriaLlamada
from Entidades.OpcionLlamada import OpcionLlamada
from Entidades.SubOpcionLlamada import SubOpcionLlamada
from Interfaces.PantallaRtaOperador import PantallaRtaOperador

# Arreglo de objetos Estado
estados: List[Estado]  = [
    Estado("EnCurso"),
    Estado("Finalizado"),
    Estado("Iniciado")
]



estadoEnCurso: Estado = None
estadoFinalizado: Estado = None
fechaHoraActual: datetime = None
fechaHoraFinLlamada: datetime = None
nombreClienteLlamada = None
descripcionCategoriaYOpcion = ""
mensajesValidacionesDeSubopcionSeleccionada = None
pantallaRegistrarRespuestaDeOperador: PantallaRtaOperador = None

class GestorRegistrarRespuestaDeOperador:
    def __init__(self, llamada: Llamada, categoriaLlamada: CategoriaLlamada):
        self.llamada = llamada
        self.categoriaLlamada = categoriaLlamada
        # Creo instancia de la pantalla
        self.pantallaRtaOperador = PantallaRtaOperador(self)
        
    def nuevaRtaOperador(self):
        
        global fechaHoraActual
        global pantallaRegistrarRespuestaDeOperador
        global nombreClienteLlamada
        global descripcionCategoriaYOpcion
        global mensajesValidacionesDeSubopcionSeleccionada
        
        # Obtengo el estado "EnCurso"
        self.buscarEstadoEnCurso()
        
        # Obtengo la fecha hora actual y la seteo a fechaHoraActualInicioLlamada
        fechaHoraActual = self.obtenerFechaHoraActual()
        
        # Seteo el estado actual de la llamada a "EnCurso"
        self.llamada.setEstadoActual(estadoEnCurso, fechaHoraActualInicioLlamada)
        
        # Obtengo datos de la llamada
        self.obtenerDatosLlamada()
        
        
        # Muestro los datos de la llamada
        self.pantallaRegistrarRespuestaDeOperador.mostrarDatosDeLaLlamada(nombreClienteLlamada, descripcionCategoriaYOpcion)

        # Muestro opciones de validacion
        self.pantallaRegistrarRespuestaDeOperador.mostrarOpcionesDeValidacion(mensajesValidacionesDeSubopcionSeleccionada)
        
        self.pantallaRegistrarRespuestaDeOperador.run()
        
    
    def buscarEstadoEnCurso(self):
        global estadoEnCurso  # Utilizar la variable global de la clase

        # Iterar sobre el arreglo de estados
        for estado in estados:
            if estado.esEnCurso():
                estadoEnCurso = estado
    
    # Devuelve la fecha y hora actual
    def obtenerFechaHoraActual(self):
        return datetime.datetime.now()
    
    # Obtiene los datos de la llamada. Son traídos desde el CU 1
    def obtenerDatosLlamada(self):
        global nombreClienteLlamada
        global descripcionCategoriaYOpcion
        global mensajesValidacionesDeSubopcionSeleccionada
        
        nombreClienteLlamada = self.llamada.getNombreClienteDeLlamada()
        descripcionCategoriaYOpcion = self.categoriaLlamada.getDescripcionCompletaCategoriaYOpcion()
        mensajesValidacionesDeSubopcionSeleccionada = self.categoriaLlamada.buscarValidaciones()


    def tomarOpcionDeValidacion(self, opcionSeleccionada):
        esInformacionCorrecta = self.llamada.cliente.esInformacionCorrecta(opcionSeleccionada)
        self.pantallaRegistrarRespuestaDeOperador.habilitarSeleccionRespuesta(esInformacionCorrecta, opcionSeleccionada)
        
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
        
    def llamarCU28(self, accion_realizar):
        pass
    
    def buscarEstadoFinalizado(self):
        global estadoFinalizado  # Utilizar la variable global de la clase

        # Iterar sobre el arreglo de estados
        for estado in estados:
            if estado.esFinalizado():
                estadoFinalizado = estado
                
    def finCU(self):
        exit()
        
    def clienteCuelgaLlamada(self, arg1, arg2):
        global fechaHoraActualInicioLlamada
        global fechaHoraFinLlamada
        global estadoFinalizado
        self.buscarEstadoFinalizado()
        fechaHoraFinLlamada = self.obtenerFechaHoraActual()
        duracion = self.llamada.calcularDuracion(fechaHoraActualInicioLlamada, fechaHoraFinLlamada)
        # Seteo el estado actual de la llamada a "Finalizado"
        self.llamada.setEstadoActual(estadoFinalizado, fechaHoraFinLlamada)
        self.llamada.setDuracion(duracion)
        self.pantallaRegistrarRespuestaDeOperador.mostrarMensajeDeLlamadaTerminada()
        self.finCU()