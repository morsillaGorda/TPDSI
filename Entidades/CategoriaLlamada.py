from typing import List
from Entidades.OpcionLlamada import OpcionLlamada

class CategoriaLlamada():
    def init(self, audioMensajeOpciones, mensajeOpciones, nombre, nroOrden, opcion: List[OpcionLlamada]):
        self.audioMensajeOpciones = audioMensajeOpciones
        self.mensajeOpciones = mensajeOpciones
        self.nombre = nombre
        self.nroOrden = nroOrden
        self.opcion = opcion

    def getAudioMensajeOpciones(self):
        return self.audioMensajeSubOpcion
