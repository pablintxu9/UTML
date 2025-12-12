class EspacioAbierto:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
        self.edificios = []

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)