class OpcionValidacion(Validacion):
    def init(self, audioMensajeValidacion, nombre, correcta, descripcion):
        super().init(audioMensajeValidacion, nombre)
        self.correcta = correcta
        self.descripcion = descripcion

    def getCorrecta(self):
        return self.correcta

    def getDescripcion(self):
        return self.descripcion
