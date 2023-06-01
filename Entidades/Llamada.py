from typing import List

from Entidades.OpcionLlamada import OpcionLlamada
from Entidades.SubOpcionLlamada import SubOpcionLlamada
from Entidades.Cliente import Cliente
from Entidades.CambioEstado import CambioEstado

class Llamada:
    def init(self, descripcionOperador, detalleAccionRequerida, cambioEstado: List[CambioEstado], cliente: Cliente, respuestas):
        self.descripcionOperador = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.duracion = 0
        self.encuestaEnviada = False
        self.observacionAuditor = ""
        self.respuestas = respuestas
        
        self.opcionSeleccionada: OpcionLlamada = None
        self.subOpcionLlamada: SubOpcionLlamada = None
        self.cambioEstado = cambioEstado
        self.cliente = cliente

    def calcularDuracion(self, inicio, fin):
        #Calcula la duración de la llamada
        self.duracion = fin - inicio

    def esDePeriodo(self, inicioPeriodo, finPeriodo):
        # Lógica para verificar si la llamada está dentro de un período específico
        pass

    def getDuracion(self):
        #Devuelve la duracion
        return self.duracion

    def getNombreClienteDeLlamada(self):
        # Lógica para obtener el nombre del cliente asociado a la llamada
        return self.cliente


    def getRespuestas(self):
        # Lógica para obtener las respuestas de la encuesta de la llamada
        return self.respuestas

    def setDescripcionOperador(self, descripcionOperador):
        self.descripcionOperador = descripcionOperador

    def setDuracion(self, duracion):
        self.duracion = duracion

    def setEstadoActual(self, estado):
        # Lógica para establecer el estado actual de la llamada
        pass
