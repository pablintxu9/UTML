class Lugar:
    def __init__(self, institucion, ciudad, pais):
        self.institucion = institucion
        self.ciudad = ciudad
        self.pais = pais
    
    def __str__(self):
        return f"{self.institucion} ({self.ciudad}, {self.pais})"
    
    def __repr__(self):
        return f"Lugar('{self.institucion}', '{self.ciudad}', '{self.pais}')"
