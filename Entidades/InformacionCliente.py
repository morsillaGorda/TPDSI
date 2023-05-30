class InformacionCliente:
    def init(self, datoAValidar):
        self.datoAValidar = datoAValidar
        self.validacion = None

    def esInformacionCorrecta(self):
        if self.validacion is not None:
            return self.validacion.esValidacion()
        else:
            return False
