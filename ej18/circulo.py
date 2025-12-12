from conica import Conica

class Circulo(Conica):
    def __init__(self, color, diametro):
        super().__init__(color)
        self.diametro = diametro

    def mostrar(self):
        super().mostrar()
        print(f"Diametro: {self.diametro}")