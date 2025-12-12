from typing import List
from .planta import Planta
from .libro import Libro

class Biblioteca:
    def __init__(self, nombre: str, direccion: str, telefono: List[str], numero_empleados: int, ano_apertura: str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = list(telefono)
        self.numero_empleados = numero_empleados
        self.ano_apertura = ano_apertura

        self.plantas: List[Planta] = []
        self.libros: List[Libro] = []

    def add_planta(self, planta: Planta) -> None:
        if planta not in self.plantas:
            self.plantas.append(planta)
            planta.set_biblioteca(self)

    def add_libro(self, libro: Libro) -> None:
        if libro not in self.libros:
            self.libros.append(libro)

    def __repr__(self) -> str:
        return f"Biblioteca({self.nombre})"
