import

class CategoriaLlamada(OpcionLlamada):
    def init(self, audioMensaje, opciones, mensajeOpciones, nombre, nroOrden):
        super().init(audioMensaje, mensajeSubOpcion, nombre, nroOrden)
        self.opciones = opciones

    def getAudioMensajeOpciones(self):
        return self.audioMensajeSubOpcion
