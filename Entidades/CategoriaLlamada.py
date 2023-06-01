from typing import List # librería integrada para manejr Listas de Objetos ante posible multiplicidad *

from Entidades.OpcionLlamada import OpcionLlamada # Importamos la relación asociación con la clase OpciónLlamada

class CategoriaLlamada():
    def init(self, audioMensajeOpciones, mensajeOpciones, nombre, nroOrden, opcion: List[OpcionLlamada]):
        # Inicializa los atributos con los valores que se recibieron
        self.audioMensajeOpciones = audioMensajeOpciones
        self.mensajeOpciones = mensajeOpciones
        self.nombre = nombre
        self.nroOrden = nroOrden
        self.opcion = opcion

    def getAudioMensajeOpciones(self):
        #Devuelve el valor del atributo "audioMensajeOpciones"
        return self.audioMensajeSubOpcion
    
    def getMensajeOpciones(self):
        #Devuelve el valor del atributo "mensajeOpciones"
        return self.mensajeOpciones
    
    def getNombre(self):
        #Devuelve el valor del atributo "nombre"
        return self.nombre
