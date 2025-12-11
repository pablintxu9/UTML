class Circulo:
    def __init__(self, color, diametro):
        self.color = color
        self.diametro = diametro
    
    def __str__(self):
        return f"Circulo(color={self.color}, diametro={self.diametro})"


class Rectangulo:
    def __init__(self, longitud, anchura, color):
        self.longitud = longitud
        self.anchura = anchura
        self.color = color
    
    def __str__(self):
        return f"Rectangulo(longitud={self.longitud}, anchura={self.anchura}, color={self.color})"


class Cuadrado:
    def __init__(self, longitud, color):
        self.longitud = longitud
        self.color = color
    
    def __str__(self):
        return f"Cuadrado(longitud={self.longitud}, color={self.color})"


class Elipse:
    def __init__(self, color, eje_mayor, eje_menor):
        self.color = color
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
    
    def __str__(self):
        return f"Elipse(color={self.color}, eje_mayor={self.eje_mayor}, eje_menor={self.eje_menor})"
