from tecnica import Tecnica
from material import Material
from subtecnica import Subtecnica
from estado_conservacion import EstadoConservacion

class Cuadro:
    def __init__(self, titulo, cronologia, pintor, subtecnica, material, autor, estado_conservacion):
        self.titulo = titulo
        self.cronologia = cronologia
        self.pintor = pintor
        self.subtecnica = subtecnica
        self.material = material
        self.autor = autor
        self.estado_conservacion = estado_conservacion
    
    def __str__(self):
        return f"{self.titulo} - {self.pintor}"
    
    def __repr__(self):
        return f"Cuadro('{self.titulo}', '{self.cronologia}')"
