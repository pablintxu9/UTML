class SitioArqueologico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.excavaciones = []

    def agregar_excavacion(self, excavacion):
        self.excavaciones.append(excavacion)