class Cuadro:
    def __init__(self, titulo, anno, tecnica, subtecnica, soporte, autor, estado):
        self.titulo = titulo
        self.anno = anno
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.autor = autor
        self.estado = estado
        self.lugar = None
    
    def set_localiza_en(self, lugar):
        self.lugar = lugar
    
    def __str__(self):
        return f"{self.titulo} ({self.anno})"
    
    def __repr__(self):
        return f"Cuadro('{self.titulo}', '{self.anno}')"
