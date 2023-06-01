from datetime import datetime # Librería integrada que maneja las fechas

from Entidades.Estado import Estado #Impotamos la relación asosiación con la clase estado


class CambioEstado:
    def init(self, fechaHoraInicio: datetime, estado: Estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado

    def esEstadoInicial(self):
        #Verifica si el estado asociado es Inicial
        return self.esIniciada()

    def esUltimoEstado(self):
        #Verififca si el estado asociado es Finalizado
        return self.esFinalizada()

    def getFechaInicio(self):
        #Obtiene la fecha y hora del cambio de estado
        return self.fechaHoraInicio

    def getNombreEstado(self):
        #Obtiene el nombre del estado asociado
        return self.estado.getNombre()


    @staticmethod
    def new(estado, fechaHoraInicio):

        return CambioEstado(fechaHoraInicio, estado)
