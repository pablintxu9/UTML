class Persona:
    def __init__(self, nombre, apellidos, rol):
        self.nombre = nombre
        self.apellidos = apellidos
        self.rol = rol
        self.proyectos = []
    
    def participa_en(self, proyecto):
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)
        if self not in proyecto.personas:
            proyecto.personas.append(self)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    def __repr__(self):
        return f"Persona('{self.nombre}', '{self.apellidos}', '{self.rol}')"
