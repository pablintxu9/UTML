class Empleado:
    def __init__(self, nombre: str, codigo: str):
        self.nombre = nombre
        self.codigo = codigo
        self.prestamos = []

    def add_prestamo(self, prestamo) -> None:
        if prestamo not in self.prestamos:
            self.prestamos.append(prestamo)

    def __repr__(self) -> str:
        return f"Empleado({self.nombre}, codigo={self.codigo})"
