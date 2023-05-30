class Cliente:
    def init(self, dni, nombreCompleto, nroCelular):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular

    def esCliente(self):
        return True

    def getNombre(self):
        return self.nombre_completo

    def getNroCelular(self):
        return self.nroCelular
