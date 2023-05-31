from Entidades.OpcionValidacion import OpcionValidacion
from Entidades.Validacion import Validacion

class InformacionCliente:
    def init(self, datoAValidar, validacion: Validacion):
        self.datoAValidar = datoAValidar
        self.validacion = validacion
        self.opcionCorrecta: OpcionValidacion = None

    def esInformacionCorrecta(self):
        if self.validacion is not None:
            return self.validacion.esValidacion()
        else:
            return False
