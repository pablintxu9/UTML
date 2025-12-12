class EntidadGeografica:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def mostrar(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")