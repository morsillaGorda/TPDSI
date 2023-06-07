from typing import List

from Entidades.InformacionCliente import InformacionCliente

class Cliente:
    def __init__(self, dni, nombreCompleto, nroCelular, info: List[InformacionCliente]):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular
        self.info = info

    def esCliente(self):
        #Devuelve el valor del atributo "dni"
        return self.dni

    def getNombre(self):
        #Devuelve el valor del atributo  "nombre"
        return self.nombre_completo

    def getNroCelular(self):
        #Devuelve el valor del atributo "nroCelular"
        return self.nroCelular

    def esInformacionCorrecta(self, opcion):
        # Verifica si el atributo "Cliente" es verdadero
        for i in self.info:
            
            return i.esInformacionCorrecta()