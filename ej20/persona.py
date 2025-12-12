class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.roles = []

    def asignar_rol(self, rol):
        self.roles.append(rol)