from Entidades.SubOpcionLlamada import SubOpcionLlamada
from Entidades.Validacion import Validacion

class OpcionLlamada:
    def init(self, audioMensajeSubOpcion, mensajeSubOpciones, nombre, nroOrden):
        self.audioMensajeSubOpcion = audioMensajeSubOpcion
        self.mensajeSubOpciones = mensajeSubOpciones
        self.nombre = nombre
        self.nroOrden = nroOrden
        self.subOpcionLlamada: SubOpcionLlamada = []
        self.validacionesRequeridas: Validacion = []

    def getAudioMensajeSubOpcion(self):
        return self.audioMensajeSubOpcion

    def getDescripcionConSubOpcion(self):
        pass

