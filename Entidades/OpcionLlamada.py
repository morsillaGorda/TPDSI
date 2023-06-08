from typing import List

from Entidades.SubOpcionLlamada import SubOpcionLlamada         #Importamos la relacion de agregacion con la clase SubOpcionLlamada
from Entidades.Validacion import Validacion         #Importamos la relacion de asociacion con la clase Validacion

class OpcionLlamada:
    def __init__(self, audioMensajeSubOpcion, mensajeSubOpciones, nombre, nroOrden, subOpcionLlamada: List[SubOpcionLlamada]):
        #Inicializamos los valores de los atributos
        self.audioMensajeSubOpcion = audioMensajeSubOpcion
        self.mensajeSubOpciones = mensajeSubOpciones
        self.nombre = nombre
        self.nroOrden = nroOrden

        self.subOpcionLlamada = subOpcionLlamada
        self.validacionesRequeridas: List[Validacion] = []

    def getAudioMensajeSubOpcion(self):
        #Devuelve el valor del atributo "audioMensajeSubOpcion"
        return self.audioMensajeSubOpcion

    def getDescripcionConSubOpcion(self):
        #Devuelve el valor de una descripcion a partir de los valores de "nombre" y "nroOrden"

        descripcion = f"{self.nombre} > { self.subOpcionLlamada[0].getNombre()}"
        return descripcion
    
    def getNombre(self):
        # Devuelve el valor del atributo 'nombre'
        return self.nombre
    
    def getNroOrden(self):
        # Devuelve el valor del atributo 'nroOrden'
        return self.nroOrden
    
    def buscarValidaciones(self):
        #Busca los valores del atributo 
        mensajesValidacion = []

        if(self.subOpcionLlamada is None or len(self.subOpcionLlamada) == 0):


            for validacion in self.validacionesRequeridas:

                mensajeValidacion = validacion.getMensajeValidacion()
                opcionesValidacion = validacion.getOpcionesValidacion
                mensajesValidacion.append([mensajeValidacion, opcionesValidacion])
        else:
            mensajesValidacion = self.subOpcionLlamada[0].buscarValidaciones()

        return mensajesValidacion
    
    

