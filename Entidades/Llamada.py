from typing import List     #Importamos algunas librerías integradas de python
from datetime import datetime

from Entidades.OpcionLlamada import OpcionLlamada           #Importamos entidadades para representar las relaciones de asociación
from Entidades.SubOpcionLlamada import SubOpcionLlamada
from Entidades.Cliente import Cliente
from Entidades.CambioEstado import CambioEstado

class Llamada:
    def __init__(self, cliente: Cliente, cambioEstado: List[CambioEstado]):
        self.descripcionOperador = ""
        self.detalleAccionRequerida = ""
        self.duracion = 0
        self.encuestaEnviada = False
        self.observacionAuditor = ""
        self.respuestas = ""
        self.operador = ""
        
        self.opcionSeleccionada: OpcionLlamada = None
        self.subOpcionLlamada: SubOpcionLlamada = None
        self.cambioEstado = cambioEstado
        self.cliente = cliente

    def calcularDuracion(self, fechaHoraInicio: datetime, fechaHoraFin: datetime):
        duracion = (fechaHoraFin - fechaHoraInicio).total_seconds()
        return duracion

    def getNombreClienteDeLlamada(self):
        # Lógica para obtener el nombre del cliente asociado a la llamada
        return self.cliente.getNombre()


    def getRespuestas(self):
        # Lógica para obtener las respuestas de la encuesta de la llamada
        return self.respuestas

    def setDescripcionOperador(self, descripcionOperador):
        self.descripcionOperador = descripcionOperador
        
    #Devuelve el valor del atributo "operador"
    def tomarOperador(self):
        return self.operador
    
    #Verifica si valor del atributo estado es "enCurso"
    def finalizarLlamada(self, estado, fechaHoraFin):
        # Lógica para establecer el estado actual de la llamada
        # Buscar el último cambio de estado en la lista de cambios de estado
        ultimoCambioEstado = None
        for cambioEstado in self.cambioEstado:
            if cambioEstado.esUltimoEstado():
                ultimoCambioEstado = cambioEstado
                 
        ultimoCambioEstado.getFechaHoraFin(fechaHoraFin) # Establecer la fecha y hora de finalización en el último cambio de estado encontrado

        nuevoCambioEstado = CambioEstado.new(fechaHoraFin, estado)  # Crear un nuevo cambio de estado con la fecha y hora de inicio = fechaHoraEstadoFin del ultimo estado y el estado proporcionados
    
        self.cambioEstado.append(nuevoCambioEstado) # Agregar el nuevo cambio de estado a la lista de cambios de estado
    
    def llamadaEnCurso(self, estado, fechaHoraFin):
        
        nuevoCambioEstado = None
        for cambioEstado in self.cambioEstado:
            if cambioEstado.esEstadoInicial():
                nuevoCambioEstado = cambioEstado
                 
       
    
        self.cambioEstado.append(nuevoCambioEstado) # Agregar el nuevo cambio de estado a la lista de cambios de estado



    def validarInformacionCliente(self, opcionSeleccionada):
        
        return self.cliente.esInformacionCorrecta(opcionSeleccionada)
