from Entidades.OpcionValidacion import OpcionValidacion     #Importamos las relaciones de asociación con las clases OpcionValidacion y Validacion
from Entidades.Validacion import Validacion

class InformacionCliente:
    def init(self, datoAValidar, validacion: Validacion):
        #Inicializa los atributos con los valores recibidos
        self.datoAValidar = datoAValidar #
        self.esInformacionCorrecta = validacion #Validación de la información del Cliente
        self.esOpcionCorrecta: OpcionValidacion = None  #Opción correcta de la validacion

    def esInformacionCorrecta(self):
        if self.validacion is not None:
            return self.validacion.esValidacion() # Devuelve True si la opción es correcta
        else:
            return False #Si no hay opción correcta, entonces la información será incorrecta
        
    def esValidacion(self):
        #Devuelve la Información Validada
        self.esInformacionCorrecta()
