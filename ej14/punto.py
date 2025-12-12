class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.poligono = None

    def set_poligono(self, poligono: "Poligono") -> None:
        self.poligono = poligono

    def __repr__(self) -> str:
        return f"Punto(x={self.x}, y={self.y})"
class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.poligono = None

    def set_poligono(self, poligono):
        self.poligono = poligono

    def __repr__(self):
        return f"Punto(x={self.x}, y={self.y})"
