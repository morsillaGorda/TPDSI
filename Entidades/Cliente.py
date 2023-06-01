from typing import List

from Entidades.InformacionCliente import InformacionCliente

class Cliente:
    def init(self, dni, nombreCompleto, nroCelular, info: List[InformacionCliente]):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular
        self.info = info

    def esCliente(self):
        # Verifica si el atributo "Cliente" es verdadero
        return self.info

    def getNombre(self):
        #Devuelve el valor del atributo  "nombre"
        return self.nombre_completo

    def getNroCelular(self):
        #Devuelve el valor del atributo "nroCelular"
        return self.nroCelular
