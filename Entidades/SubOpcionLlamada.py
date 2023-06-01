from typing import List #Importamos una librería integrada para crear listas de Objetos
from Entidades.Validacion import Validacion #Importamos la relacion de asociación con la clase Validacion

class SubOpcionLlamada:
    def __init__(self, nombre, nroOrden):
        # Inicializa los atributos con los valores recibidos
        self.nombre = nombre
        self.nroOrden = nroOrden
        self.validacionRequerida: List[Validacion] = []

    def esNro(self, numero):
        # Devuelve el valor del atributo "nroOrden"
        return self.nroOrden

    def getNombre(self):
        #Devuelve el valor del atributo "nombre"
        return self.nombre
    
    def buscarValidaciones(self):
         # Crea una lista vacía para almacenar los mensajes de validación
        mensajesValidacion = []
        
        # Itera sobre cada objeto de Validación en la lista validacionRequerida
        for validacion in self.validacionRequerida:
            mensajeValidacion = Validacion.getMensajeValidacion()
            mensajesValidacion.append(mensajeValidacion)
        
        # Devuelve la lista de mensajes de validación
        return mensajesValidacion
    
    
