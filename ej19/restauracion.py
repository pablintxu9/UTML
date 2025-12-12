class Restauracion:
    def __init__(self, fecha, descripcion, tecnicas):
        self.fecha = fecha
        self.descripcion = descripcion
        self.tecnicas = tecnicas
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)