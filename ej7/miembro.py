class Miembro:
    def __init__(self, nombre, apellidos, rol):
        self.nombre = nombre
        self.apellidos = apellidos
        self.rol = rol
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    def __repr__(self):
        return f"Miembro('{self.nombre}', '{self.apellidos}', '{self.rol}')"
