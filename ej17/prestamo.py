from typing import List, Optional
from datetime import date

class Prestamo:
    def __init__(self, fecha_inicio: str, fecha_estipulada: str, fecha_real_de_devolucion: Optional[str] = None):
        self.fecha_inicio = fecha_inicio
        self.fecha_estipulada = fecha_estipulada
        self.fecha_real_de_devolucion = fecha_real_de_devolucion

        self.lector = None
        self.empleado = None
        self.ejemplares: List[object] = []

    def set_lector(self, lector) -> None:
        self.lector = lector
        if self not in lector.prestamos:
            lector.add_prestamo(self)

    def set_empleado(self, empleado) -> None:
        self.empleado = empleado
        if self not in empleado.prestamos:
            empleado.add_prestamo(self)

    def add_ejemplar(self, ejemplar) -> None:
        if ejemplar not in self.ejemplares:
            self.ejemplares.append(ejemplar)
            ejemplar.add_prestamo(self)

    def __repr__(self) -> str:
        return f"Prestamo({self.fecha_inicio} -> {self.fecha_estipulada})"
