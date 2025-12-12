from typing import List
from .tematica import Tematica

class Planta:
    def __init__(self, numero: int, capacidad: int):
        self.numero = numero
        self.capacidad = capacidad
        self.biblioteca = None
        self.tematicas: List[Tematica] = []

    def set_biblioteca(self, biblioteca) -> None:
        self.biblioteca = biblioteca

    def add_tematica(self, tematica: Tematica) -> None:
        if tematica not in self.tematicas:
            self.tematicas.append(tematica)

    def __repr__(self) -> str:
        return f"Planta(numero={self.numero}, capacidad={self.capacidad})"
