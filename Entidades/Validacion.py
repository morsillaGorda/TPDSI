from typing import List
from Entidades.OpcionValidacion import OpcionValidacion

class Validacion:
    def init(self, audioMensajeValidacion, nombre, opcionesValidacion: List[OpcionValidacion]):
        self.audioMensajeValidacion = audioMensajeValidacion
        self.nombre = nombre
        self.opcionesValidacion = opcionesValidacion

    def getAudioMensajeValidacion(self):
        return self.audioMensajeValidacion

    def getMensajeValidacion(self):
        pass
