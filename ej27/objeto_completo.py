class ObjetoCompleto(ObjetoArqueologico):
    def __init__(self, codigo, descripcion, materiales, usos, datacion=None, dimensiones=None):
        super().__init__(codigo, descripcion, materiales, datacion, dimensiones)
        self.usos = usos