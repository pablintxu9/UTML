class Edificio:
    def __init__(self, numero, espacio_abierto):
        self.numero = numero
        self.espacio_abierto = espacio_abierto
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)