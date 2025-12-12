class Lector:
    def __init__(self, nombre: str, numero_identificacion: str, direccion: str):
        self.nombre = nombre
        self.numero_identificacion = numero_identificacion
        self.direccion = direccion
        self.prestamos = []

    def add_prestamo(self, prestamo) -> None:
        if prestamo not in self.prestamos:
            self.prestamos.append(prestamo)

    def __repr__(self) -> str:
        return f"Lector({self.nombre})"
