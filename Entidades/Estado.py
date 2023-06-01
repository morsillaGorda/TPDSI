class Estado:
    def init(self, nombre):
        # Inicializa el atributo "nombre" con el valor proporcionado
        self.nombre = nombre 

    def esFinalizada(self):
        # Lógica para verificar si el estado es finalizado con un booleano
        return self.nombre == "Finalizado"

    def esEnCurso(self):
        # Lógica para verificar si el estado es En Curso con un booleano
        return self.nombre == "Es en curso"

    def getNombre(self):
        # Obtiene el nombre del estado
        return self.nombre

