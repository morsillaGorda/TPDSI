class OpcionValidacion():
    def init(self, correcta, descripcion):
        self.correcta = correcta
        self.descripcion = descripcion

    def getCorrecta(self):
        return self.correcta

    def getDescripcion(self):
        return self.descripcion
