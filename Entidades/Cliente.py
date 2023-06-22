from typing import List

from Entidades.InformacionCliente import InformacionCliente

class Cliente:
    def __init__(self, dni, nombreCompleto, info: List[InformacionCliente]):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = ""
        self.info = info

    def esCliente(self):
        #Devuelve el valor del atributo "dni"
        return self.dni

    def getNombre(self):
        #Devuelve el valor del atributo  "nombre"
        return self.nombreCompleto

    def esInformacionCorrecta(self, opcion):
        # Verifica si el atributo "Cliente" es verdadero
        for informacion in self.info:
            esValdacion = informacion.esValidacion(opcion)
            esCorrecta = informacion.esInformacionCorrecta() 
            if (esCorrecta and esValdacion):
                return True
        return False