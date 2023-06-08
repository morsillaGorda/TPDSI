from Entidades.OpcionValidacion import OpcionValidacion     #Importamos las relaciones de asociación con las clases OpcionValidacion y Validacion
from Entidades.Validacion import Validacion

class InformacionCliente:
    def __init__(self, datoAValidar, validacion: Validacion):
        #Inicializa los atributos con los valores recibidos
        self.datoAValidar = datoAValidar # Dato a validar
        self.validacion = validacion #Validación de la información del Cliente
        self.esOpcionCorrecta: OpcionValidacion = None  #Opción correcta de la validacion

    def esInformacionCorrecta(self):
        if self.esOpcionCorrecta is not None:
            return self.esOpcionCorrecta.esCorrecta()  # Devuelve True si la opción correcta es correcta
        else:
            return False  # No hay opción correcta, por lo tanto la información no es correcta
    
    def esValidacion(self, validacion):
        if self.datoAValidar == validacion:
            return True
        else:
            return False
