from entidad_geografica import EntidadGeografica
from punto import Punto

class Linea(EntidadGeografica):
    def __init__(self, codigo, nombre, puntos):
        super().__init__(codigo, nombre)
        if len(puntos) < 2:
            raise ValueError("Una línea debe tener al menos 2 puntos.")
        self.puntos = puntos

    def mostrar(self):
        super().mostrar()
        print("Línea definida por los puntos:")
        for p in self.puntos:
            p.mostrar()