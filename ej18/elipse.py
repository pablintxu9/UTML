from conica import Conica

class Elipse(Conica):
    def __init__(self, color, eje_mayor, eje_menor):
        super().__init__(color)
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def mostrar(self):
        super().mostrar()
        print(f"Eje Mayor: {self.eje_mayor}")
        print(f"Eje Menor: {self.eje_menor}")