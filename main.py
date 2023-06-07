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


opcionValidacion1a: OpcionValidacion = OpcionValidacion(True, 3)
opcionValidacion1b: OpcionValidacion = OpcionValidacion(False, 6)
opcionValidacion1c: OpcionValidacion = OpcionValidacion(False, 1)
tipoInformacion1: TipoInformacion = TipoInformacion("Cantidad de hijos")
validacion1: Validación = Validación("Ingrese cantidad de hijos",
                                     "CantidadDeHijos",
                                     [opcionValidacion1a, opcionValidacion1b, opcionValidacion1c],
                                     tipoInformacion1)

opcionValidacion2a: OpcionValidacion = OpcionValidacion(False, "5000")
opcionValidacion2b: OpcionValidacion = OpcionValidacion(True, "5001")
opcionValidacion2c: OpcionValidacion = OpcionValidacion(False, "5003")
tipoInformacion2: TipoInformacion = TipoInformacion("Código postal")
validacion2: Validación = Validación("Ingrese el código postal",
                                     "codigoPostal",
                                     [opcionValidacion2a, opcionValidacion2b, opcionValidacion2c],
                                     tipoInformacion2)

informacionCliente1: InformacionCliente = InformacionCliente(3, validacion1, tipoInformacion1)
informacionCliente1.opcionCorrecta = opcionValidacion1a

informacionCliente2: InformacionCliente = InformacionCliente("5001", validacion2, tipoInformacion2)
informacionCliente2.opcionCorrecta = opcionValidacion2b



cliente1: Cliente = Cliente("44987546", "Juan Perez", [informacionCliente1, informacionCliente2])

estadoInicial: Estado = Estado("Iniciado")


cambioEstadoInicial: CambioEstado = CambioEstado(datetime.datetime.now(), estadoInicial)

llamada: Llamada = Llamada(cliente1, [cambioEstadoInicial])


subOpcionLlamadaRobo2a: SubOpcionLlamada = SubOpcionLlamada("Titular", 1)
subOpcionLlamadaRobo2b: SubOpcionLlamada = SubOpcionLlamada("Extension", 2)

subOpcionLlamadaRobo2a.validacionRequerida = [validacion1, validacion2]

subOpcionesLlamadaRobo2: List[SubOpcionLlamada] = [subOpcionLlamadaRobo2a]
opcionLlamadaRobo1: OpcionLlamada = OpcionLlamada("Informar robo", "Informar robo", "Informar robo", 1, [])

opcionLlamadaRobo2: OpcionLlamada = OpcionLlamada("Solicitar nueva tarjeta de crédito",
                                                  "Solicitar nueva tarjeta de crédito",
                                                  "Solicitar nueva tarjeta de credito", 2, subOpcionesLlamadaRobo2)

opcionLlamadaRobo3: OpcionLlamada = OpcionLlamada("Solicitar cancelación de la tarjeta de crédito",
                                                  "Solicitar cancelación de la tarjeta de crédito",
                                                  "Solicitar cancelacion de la tarjetaDeCredito", 3, [])

opcionesCategoriaLlamadaRobo: List[OpcionLlamada] = [
    # opcionLlamadaRobo1,
    opcionLlamadaRobo2,
    # opcionLlamadaRobo3
]

categoriaLlamadaRobo: CategoriaLlamada = CategoriaLlamada(
    "Seleccione opcion para el robo de tarjeta:",
    "Seleccione opcion para el robo de tarjeta:",
    "Robo de tarjeta",
    1,
    opcionesCategoriaLlamadaRobo
)

if __name__ == "__main__":
    # Crear una instancia de GestorRegistrarRespuestaDeOperador
    gestor = GestorRtaOperador(llamada, categoriaLlamadaRobo)

    # Llamar al método respuestaOperador
    gestor.nuevaRtaOperador()