# Importación de librerías propias de python
import datetime
from typing import List

# Importación de Entidades
from Entidades.Estado import Estado
from Entidades.Llamada import Llamada
from Entidades.CategoriaLlamada import CategoriaLlamada
from Entidades.Cliente import Cliente
from Interfaces.PantallaRtaOperador import PantallaRegistrarRespuestaDeOperador

# Array con los diferentes estados del objeto Estado
estados: List[Estado]  = [
    Estado("EnCurso"),
    Estado("Finalizado"),
    Estado("Iniciado")
]

#Datos que puede guardar el Gestor

datosLlamadas = None
estadoEnCurso = None
estadoFinalizada = None
InformaciónCliente = None
llamada = None
operador = ""
pantallaOperador = None
validaciones = None


class GestorRtaOperador:
    def __init__(self, llamada: Llamada, categoriaLlamada: CategoriaLlamada,opcionLlamada: OpcionLlamada, subopcionLlamada: SubOpcionLlamada):
        self.llamada = llamada
        self.categoriaLlamada = categoriaLlamada
        self.opcionLlamada = opcionLlamada
        self.subopcionLlamada = subopcionLlamada

    def nuevaRtaOperador(self):

        global fechaHoraActual