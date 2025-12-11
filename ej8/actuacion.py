from tipo_actuacion import TipoActuacion

class Actuacion:
    def __init__(self, fecha_inicio, fecha_fin, tipo):
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo
    
    def __str__(self):
        return f"Actuación ({self.tipo.value}) - {self.fecha_inicio} a {self.fecha_fin}"
    
    def __repr__(self):
        return f"Actuacion('{self.fecha_inicio}', '{self.fecha_fin}', {self.tipo})"
