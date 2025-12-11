class Proyecto:
    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.personas = []
        self.lugares = []
    
    def agregar_persona(self, persona):
        if persona not in self.personas:
            self.personas.append(persona)
        if self not in persona.proyectos:
            persona.proyectos.append(self)
    
    def tiene_lugar_en(self, lugar):
        if lugar not in self.lugares:
            self.lugares.append(lugar)
    
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return f"Proyecto('{self.nombre}')"
