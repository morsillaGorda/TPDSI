from typing import List
from Entidades.Validacion import Validacion

class SubOpcionLlamada:
    def init(self, nombre, nroOrden):
        self.nombre = nombre
        self.nroOrden = nroOrden
        self.validacionRequerida: List[Validacion] = []

    def esNro(self, numero):
        # Lógica para verificar si el número coincide con el nroOrden
        pass

    def getNombre(self):
        return self.nombre
