from datetime import datetime # Librería integrada que maneja las fechas

from Entidades.Estado import Estado #Impotamos la relación asosiación con la clase estado


class CambioEstado:
    def __init__(self, fechaHoraInicio: datetime, estado: Estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado
        self.fechaHoraFin = None

    def esEstadoInicial(self):
        #Verifica si el estado asociado es Inicial
        return self.estado.esIniciado()

    def esUltimoEstado(self):
        #Verififca si el estado asociado es Finalizado
        return self.fechaHoraFin is None

    def getFechaHoraInicio(self):
        #Obtiene la fecha y hora del cambio de estado
        return self.fechaHoraInicio
    
    def getFechaHoraFin(self, fechaHoraFin):
        #Seteo de FechaHoraFin
        self.fechaHoraFin = fechaHoraFin  

    def getNombreEstado(self):
        #Obtiene el nombre del estado asociado
        return self.estado.getNombre()


    @staticmethod
    def new(estado, fechaHoraInicio):

        return CambioEstado(fechaHoraInicio, estado)
