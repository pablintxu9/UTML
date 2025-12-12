from proyecto import Proyecto

class Intervencion:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.actuaciones = []

    def agregar_actuacion(self, actuacion):
        self.actuaciones.append(actuacion)