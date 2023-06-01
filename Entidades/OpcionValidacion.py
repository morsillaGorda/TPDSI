class OpcionValidacion():
    def __init__(self, correcta, descripcion):
        #Inicializa los atributos con los valores recibidos
        self.correcta = correcta
        self.descripcion = descripcion

    def getCorrecta(self):
        #Devuelve el valor del atributo "correcta"
        return self.correcta

    def getDescripcion(self):
        #Devuelve el valor del atributo "descripcion"
        return self.descripcion
