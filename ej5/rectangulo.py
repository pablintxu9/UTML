class Rectangulo:
    def __init__(self, longitud, anchura, color):
        self.longitud = longitud
        self.anchura = anchura
        self.color = color
    
    def __str__(self):
        return f"Rectangulo(longitud={self.longitud}, anchura={self.anchura}, color={self.color})"
