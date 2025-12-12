from forma import Forma

class Cuadrilatero(Forma):
    def __init__(self, color, longitud):
        super().__init__(color)
        self.longitud = longitud

    def mostrar(self):
        super().mostrar()
        print(f"Longitud: {self.longitud}")