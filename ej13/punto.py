class Punto:
    def __init__(self, x, y, poligono=None):
        self.x = x
        self.y = y
        self.poligono = poligono

    def set_poligono(self, poligono):
        if self.poligono is poligono:
            return
        if self.poligono is not None and poligono is not None:
            raise ValueError("El punto ya pertenece a otro polígono")
        self.poligono = poligono

    def __str__(self):
        return f"Punto(x={self.x}, y={self.y})"

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"
