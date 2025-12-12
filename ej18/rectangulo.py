from cuadrilatero import Cuadrilatero

class Rectangulo(Cuadrilatero):
    def __init__(self, color, longitud, anchura):
        super().__init__(color, longitud)
        self.anchura = anchura

    def mostrar(self):
        super().mostrar()
        print(f"Anchura: {self.anchura}")