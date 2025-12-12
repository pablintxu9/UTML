from entidad_geografica import EntidadGeografica

class Punto(EntidadGeografica):
    def __init__(self, codigo, nombre, x, y, z):
        super().__init__(codigo, nombre)
        self.x = x
        self.y = y
        self.z = z

    def mostrar(self):
        super().mostrar()
        print(f"Coordenadas: X={self.x}, Y={self.y}, Z={self.z}")