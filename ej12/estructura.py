from material import Material

class Estructura:
    def __init__(self, codigo, datacion):
        self.codigo = codigo
        self.datacion = datacion
        self.materiales = []
        self.estructura_marco = None
        self.subestructuras = []

    def agregar_material(self, material):
        if isinstance(material, Material) and material not in self.materiales:
            self.materiales.append(material)

    def set_estructura_marco(self, estructura):
        if estructura is self:
            return
        self.estructura_marco = estructura
        if self not in estructura.subestructuras:
            estructura.subestructuras.append(self)

    def agregar_subestructura(self, sub):
        if sub is self:
            return
        if sub not in self.subestructuras:
            self.subestructuras.append(sub)
        if sub.estructura_marco is not self:
            sub.estructura_marco = self

    def __str__(self):
        return f"Estructura {self.codigo} ({self.datacion})"

    def __repr__(self):
        return f"Estructura('{self.codigo}', '{self.datacion}')"
