class Lugar:
    def __init__(self, nombre, coordenada_x, coordenada_y):
        self.nombre = nombre
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
    
    def __str__(self):
        return f"{self.nombre} ({self.coordenada_x}, {self.coordenada_y})"
    
    def __repr__(self):
        return f"Lugar('{self.nombre}', {self.coordenada_x}, {self.coordenada_y})"
