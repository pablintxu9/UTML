from enum import Enum

class Tecnica(Enum):
    OLEO = "Óleo"
    ACUARELA = "Acuarela"
    PASTEL = "Pastel"
    FRESCO = "Fresco"

class Material(Enum):
    ALAMO = "Álamo"
    NOGAL = "Nogal"
    LIENZO = "Lienzo"
    MADERA = "Madera"

class Subtecnica(Enum):
    SFUMATO = "Sfumato"
    PINCELADO_SIMPLE = "Pincelado simple"
    COLLAGE = "Collage"
    VELADURA = "Veladura"

class EstadoConservacion(Enum):
    EXCELENTE = "Excelente"
    BUENO = "Bueno"
    REGULAR = "Regular"
    MALO = "Malo"
    DESTRUIDO = "Destruido"

class Cuadro:
    def __init__(self, titulo, cronologia, tecnica, subtecnica, material, autor, estado):
        self.titulo = titulo
        self.cronologia = cronologia
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.material = material
        self.autor = autor
        self.estado = estado
        self.lugar = None
        self.original = None
        self.replicas = []

    def set_localiza_en(self, lugar):
        self.lugar = lugar

    def set_original(self, original):
        if original is self:
            return
        self.original = original
        if self not in original.replicas:
            original.replicas.append(self)

    def add_replica(self, replica):
        if replica is self:
            return
        if replica not in self.replicas:
            self.replicas.append(replica)
        if replica.original is not self:
            replica.original = self

    def __str__(self):
        return f"{self.titulo} ({self.cronologia})"

    def __repr__(self):
        return f"Cuadro('{self.titulo}', '{self.cronologia}')"
