from typing import List     #Importamos librería integrada para crear listas de Objetos
from Entidades.OpcionValidacion import OpcionValidacion #Importamos la relacion de agregacion con la clase OpcionValidacion

class Validacion:
    def __init__(self, audioMensajeValidacion, nombre, opcionesValidacion: List[OpcionValidacion]):
        #Inicializamos los valores de los atributos
        self.audioMensajeValidacion = audioMensajeValidacion
        self.nombre = nombre
        self.opcionesValidacion = opcionesValidacion

    def getAudioMensajeValidacion(self):
        # Devuelve el valor del atributo 'audioMensajeValidacion'
        return self.audioMensajeValidacion

    def getMensajeValidacion(self):
         # Crea una lista vacía para almacenar los mensajes de validación
        mensajesValidacion = []
        
        # Itera sobre cada objeto de Validación en la lista validacionRequerida
        for opcValidacion in self.validacionRequerida:
            mensajeValidacion = OpcionValidacion.getCorrecta()
            mensajesValidacion.append(mensajeValidacion)
        
        # Devuelve la lista de mensajes de validación
        return mensajesValidacion

