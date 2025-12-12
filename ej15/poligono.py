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
