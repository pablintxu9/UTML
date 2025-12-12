from espacio_abierto import EspacioAbierto

class Plaza(EspacioAbierto):
    def __init__(self, nombre, superficie, ciudad):
        super().__init__(nombre, ciudad)
        self.superficie = superficie