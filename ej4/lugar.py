class Lugar:
    def __init__(self, ciudad, comunidad, pais):
        self.ciudad = ciudad
        self.comunidad = comunidad
        self.pais = pais
    
    def __str__(self):
        return f"{self.ciudad} ({self.comunidad}, {self.pais})"
    
    def __repr__(self):
        return f"Lugar('{self.ciudad}', '{self.comunidad}', '{self.pais}')"
