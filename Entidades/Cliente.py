from typing import List

from Entidades.InformacionCliente import InformacionCliente

class Cliente:
    def init(self, dni, nombreCompleto, nroCelular, info: List[InformacionCliente]):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular
        self.info = info

    def esCliente(self):
        return True

    def getNombre(self):
        return self.nombre_completo

    def getNroCelular(self):
        return self.nroCelular
