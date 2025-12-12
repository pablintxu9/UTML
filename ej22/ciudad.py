class Ciudad:
    def __init__(self, nombre, provincia, pais):
        self.nombre = nombre
        self.provincia = provincia
        self.pais = pais
        self.espacios_abiertos = []

    def agregar_espacio(self, espacio):
        self.espacios_abiertos.append(espacio)