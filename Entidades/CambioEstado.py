from datetime import datetime

from Entidades.Estado import Estado


class CambioEstado:
    def init(self, fechaHoraInicio: datetime, estado: Estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado

    def esEstadoInicial(self):
        return self.estado.esIniciada()

    def esUltimoEstado(self):
        return self.estado.esFinalizada()

    def getFechaInicio(self):
        return self.fechaHoraInicio

    def getNombreEstado(self):
        return self.estado.getNombre()


    @staticmethod
    def new(estado, fechaHoraInicio):

        return CambioEstado(fechaHoraInicio, estado)
