class Coleccion:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)