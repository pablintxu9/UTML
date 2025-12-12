class EntidadArqueologica:
    def __init__(self, cronologia):
        self.cronologia = cronologia
        self.lugar = None
        self.dimensiones = []

    def asignar_lugar(self, lugar):
        self.lugar = lugar

    def agregar_dimension(self, dimension):
        self.dimensiones.append(dimension)