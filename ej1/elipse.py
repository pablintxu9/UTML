class Elipse:
    def __init__(self, color, eje_mayor, eje_menor):
        self.color = color
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
    
    def __repr__(self):
        return f"Elipse(color='{self.color}', eje_mayor={self.eje_mayor}, eje_menor={self.eje_menor})"
