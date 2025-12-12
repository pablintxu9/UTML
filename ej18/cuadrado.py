from rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    def __init__(self, color, lado):
        super().__init__(color, lado, lado)