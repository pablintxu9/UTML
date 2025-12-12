class ObjetoArqueologico:
    def __init__(self, codigo, descripcion, materiales, datacion=None, dimensiones=None):
        self.codigo = codigo
        self.descripcion = descripcion
        self.materiales = materiales
        self.datacion = datacion
        self.dimensiones = dimensiones
        self.similares = []

    def agregar_similar(self, otro_objeto):
        self.similares.append(otro_objeto)