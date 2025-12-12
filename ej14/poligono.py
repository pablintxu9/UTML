from typing import List
from .punto import Punto

class Poligono:
    def __init__(self):
        self._puntos: List[Punto] = []

    def agregar_punto(self, punto: Punto) -> None:
        if punto not in self._puntos:
            self._puntos.append(punto)
            punto.set_poligono(self)

    def get_puntos(self) -> List[Punto]:
        return list(self._puntos)

    def __repr__(self) -> str:
        return f"Poligono(puntos={self._puntos})"
class Poligono:
    def __init__(self):
        self.puntos = []

    def agregar_punto(self, punto):
        if punto.poligono is not None and punto.poligono is not self:
            raise ValueError("El punto ya pertenece a otro polígono")
        punto.set_poligono(self)
        self.puntos.append(punto)

    def __repr__(self):
        return f"Poligono(puntos={self.puntos})"
