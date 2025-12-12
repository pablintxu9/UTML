from typing import List

class Tematica:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros = []

    def add_libro(self, libro) -> None:
        if libro not in self.libros:
            self.libros.append(libro)

    def __repr__(self) -> str:
        return f"Tematica({self.nombre})"
