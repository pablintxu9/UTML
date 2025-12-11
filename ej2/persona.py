class Persona:
    def __init__(self, nombre, apellido, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.parejas = []
        self.hijos = []
        self.padres = []
    
    def casarse_con(self, otra_persona):
        if otra_persona not in self.parejas:
            self.parejas.append(otra_persona)
        if self not in otra_persona.parejas:
            otra_persona.parejas.append(self)
    
    def agregar_hijo(self, hijo):
        if hijo not in self.hijos:
            self.hijos.append(hijo)
        if self not in hijo.padres:
            hijo.padres.append(self)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def __repr__(self):
        return f"Persona('{self.nombre}', '{self.apellido}', '{self.sexo}')"
