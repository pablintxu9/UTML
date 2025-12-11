class Proyecto:
    def __init__(self, nombre, fecha_inicio, fecha_fin):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.miembros = []
        self.lugares_actuacion = []
    
    def agregar_miembro(self, miembro):
        if miembro not in self.miembros:
            self.miembros.append(miembro)
    
    def agregar_lugar(self, lugar):
        if lugar not in self.lugares_actuacion:
            self.lugares_actuacion.append(lugar)
    
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return f"Proyecto('{self.nombre}')"
