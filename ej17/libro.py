from typing import List
from .tematica import Tematica
from .ejemplar import Ejemplar

class Libro:
    def __init__(self, isbn: str, titulo: str, ano_publicacion: str, idiomas: List[str]):
        self.isbn = isbn
        self.titulo = titulo
        self.ano_publicacion = ano_publicacion
        self.idiomas = list(idiomas)

        self.tematicas: List[Tematica] = []
        self.ejemplares: List[Ejemplar] = []

    def add_tematica(self, tematica: Tematica) -> None:
        if tematica not in self.tematicas:
            self.tematicas.append(tematica)
            tematica.add_libro(self)

    def add_ejemplar(self, ejemplar: Ejemplar) -> None:
        if ejemplar not in self.ejemplares:
            self.ejemplares.append(ejemplar)
            ejemplar.libro = self

    def __repr__(self) -> str:
        return f"Libro({self.titulo}, ISBN={self.isbn})"
