from espacio_abierto import EspacioAbierto

class Calle(EspacioAbierto):
    def __init__(self, nombre, longitud, ciudad):
        super().__init__(nombre, ciudad)
        self.longitud = longitud