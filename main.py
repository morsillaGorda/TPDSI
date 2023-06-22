from typing import List
from datetime import datetime

from Controladores.GestorRtaOperador import GestorRtaOperador
from Entidades.CategoriaLlamada import CategoriaLlamada
from Entidades.OpcionValidacion import OpcionValidacion
from Entidades.SubOpcionLlamada import SubOpcionLlamada
from Entidades.Validacion import Validacion
from Entidades.InformacionCliente import InformacionCliente
from Entidades.Cliente import Cliente
from Entidades.Estado import Estado
from Entidades.CambioEstado import CambioEstado
from Entidades.Llamada import Llamada
from Entidades.OpcionLlamada import OpcionLlamada


opcionValidacion1a: OpcionValidacion = OpcionValidacion(False, "21-02-09")
opcionValidacion1b: OpcionValidacion = OpcionValidacion(False,"10-07-12")
opcionValidacion1c: OpcionValidacion = OpcionValidacion(True, "14-06-08")

validacion1: Validacion = Validacion ("Ingrese fecha de nacimiento","Fecha de nacimiento",[opcionValidacion1a, opcionValidacion1b, opcionValidacion1c],)
                                     
                                     

opcionValidacion2a: OpcionValidacion = OpcionValidacion(False, "24")
opcionValidacion2b: OpcionValidacion = OpcionValidacion(True, "48")
opcionValidacion2c: OpcionValidacion = OpcionValidacion(False, "34")

validacion2: Validacion = Validacion("Ingrese su edad","Edad",[opcionValidacion2a, opcionValidacion2b, opcionValidacion2c],)

informacionCliente1: InformacionCliente = InformacionCliente("14-06-08", validacion1)
informacionCliente1.esOpcionCorrecta = opcionValidacion1c

informacionCliente2: InformacionCliente = InformacionCliente("48", validacion2)
informacionCliente2.esOpcionCorrecta = opcionValidacion2b



cliente1: Cliente = Cliente("40675121", "Bruno Bobadilla", [informacionCliente1, informacionCliente2])

estadoInicial: Estado = Estado("Iniciado")


cambioEstadoInicial: CambioEstado = CambioEstado(datetime.now(), estadoInicial)

llamada: Llamada = Llamada(cliente1, [cambioEstadoInicial])


subOpcionLlamadaExtravio2a: SubOpcionLlamada = SubOpcionLlamada("Titular", 1)
subOpcionLlamadaExtravio2b: SubOpcionLlamada = SubOpcionLlamada("Extension", 2)

subOpcionLlamadaExtravio2a.validacionRequerida = [validacion1, validacion2]

subOpcionesLlamadaExtravio2: List[SubOpcionLlamada] = [subOpcionLlamadaExtravio2a]
opcionLlamadaExtravio1: OpcionLlamada = OpcionLlamada("Informar extravio", "Informar extravio", "Informar extravio", 1, [])

opcionLlamadaExtravio2: OpcionLlamada = OpcionLlamada("Solicitar nueva tarjeta de crédito",
                                                  "Solicitar nueva tarjeta de crédito",
                                                  "Solicitar nueva tarjeta de credito", 2, subOpcionesLlamadaExtravio2)

opcionLlamadaExtravio3: OpcionLlamada = OpcionLlamada("Solicitar cancelación de la tarjeta de crédito",
                                                  "Solicitar cancelación de la tarjeta de crédito",
                                                  "Solicitar cancelacion de la tarjetaDeCredito", 3, [])

opcionesCategoriaLlamadaExtravio: List[OpcionLlamada] = [
    # opcionLlamadaExtravio1,
      opcionLlamadaExtravio2,
    # opcionLlamadaExtravio3
]

categoriaLlamadaRobo: CategoriaLlamada = CategoriaLlamada(
    "Seleccione opcion para nueva tarjeta de credito:",
    "Seleccione opcion para nueva tarjeta de credito",
    "Extravio de tarjeta de credito",
    1,
    opcionesCategoriaLlamadaExtravio
)



if __name__ == "__main__":
    # Crear una instancia de GestorRegistrarRespuestaDeOperador
    gestor = GestorRtaOperador(llamada, categoriaLlamadaRobo)

    # Llamar al método respuestaOperador
    gestor.nuevaRtaOperador()
    