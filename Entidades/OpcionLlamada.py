class OpcionLlamada:
    def init(self, audioMensajeSubOpcion, mensajeSubOpcion, nombre, nroOrden):
        self.audioMensajeSubOpcion = audioMensajeSubOpcion
        self.mensajeSubOpcion = mensajeSubOpcion
        self.nombre = nombre
        self.nroOrden = nroOrden
        self.subopciones = []

    def getAudioMensajeSubOpcion(self):
        return self.audioMensajeSubOpcion

    def getDescripcionConSubOpcion(self):
        pass

