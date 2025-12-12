class Ejemplar:
    def __init__(self, codigo: str, editorial: str, ano_adquisicion: str):
        self.codigo = codigo
        self.editorial = editorial
        self.ano_adquisicion = ano_adquisicion
        self.libro = None
        self.prestamos = []

    def add_prestamo(self, prestamo) -> None:
        if prestamo not in self.prestamos:
            self.prestamos.append(prestamo)

    def esta_disponible(self) -> bool:
        return not any(p.fecha_real_de_devolucion is None for p in self.prestamos)

    def __repr__(self) -> str:
        return f"Ejemplar(codigo={self.codigo})"
