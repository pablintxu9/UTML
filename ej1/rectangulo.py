class Rectangulo:
    def __init__(self, longitud, anchura, color):
        self.longitud = longitud
        self.anchura = anchura
        self.color = color
    
    def __repr__(self):
        return f"Rectángulo(longitud={self.longitud}, anchura={self.anchura}, color='{self.color}')"
