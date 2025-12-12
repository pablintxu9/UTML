class Edificio:
    def __init__(self, codigo):
        self.codigo = codigo
        self.usos = []

    def agregar_uso(self, uso_edificio):
        self.usos.append(uso_edificio)