from entidad_geografica import EntidadGeografica
from punto import Punto

class Area(EntidadGeografica):
    def __init__(self, codigo, nombre, puntos):
        super().__init__(codigo, nombre)
        if len(puntos) < 3:
            raise ValueError("Un área debe tener al menos 3 puntos.")
        self.puntos = puntos

    def mostrar(self):
        super().mostrar()
        print("Área definida por los puntos:")
        for p in self.puntos:
            p.mostrar()