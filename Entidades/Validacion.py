from typing import List     #Importamos librería integrada para crear listas de Objetos
from Entidades.OpcionValidacion import OpcionValidacion #Importamos la relacion de agregacion con la clase OpcionValidacion

class Validacion:
    def init(self, audioMensajeValidacion, nombre, opcionesValidacion: List[OpcionValidacion]):
        #Inicializamos los valores de los atributos
        self.audioMensajeValidacion = audioMensajeValidacion
        self.nombre = nombre
        self.opcionesValidacion = opcionesValidacion

    def getAudioMensajeValidacion(self):
        # Devuelve el valor del atributo 'audioMensajeValidacion'
        return self.audioMensajeValidacion

    def getMensajeValidacion(self):
        mensajeValidacion = self.opcionesValidacion
        return mensajeValidacion

    def getCorrecta(self):
        #Verifica si la opcion es correcta
        return self.opcionesValidacion
