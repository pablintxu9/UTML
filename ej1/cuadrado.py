class Cuadrado:
    def __init__(self, longitud, color):
        self.longitud = longitud
        self.color = color
    
    def __repr__(self):
        return f"Cuadrado(longitud={self.longitud}, color='{self.color}')"
