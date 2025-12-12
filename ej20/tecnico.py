from rol import Rol

class Tecnico(Rol):
    def __init__(self, persona):
        super().__init__(persona)
        self.intervenciones = []

    def agregar_intervencion(self, intervencion):
        self.intervenciones.append(intervencion)