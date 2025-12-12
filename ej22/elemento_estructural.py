from tipo_elemento import TipoElemento

class ElementoEstructural:
    def __init__(self, tipo, edificio):
        if tipo not in TipoElemento.TODOS:
            raise ValueError("Tipo de elemento no válido.")
        self.tipo = tipo
        self.edificio = edificio