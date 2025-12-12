class Excavacion:
    def __init__(self, fecha_inicio, fecha_fin=None):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.objetos = []

    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)