class FragmentoObjeto(ObjetoArqueologico):
    def __init__(self, codigo, descripcion, materiales, datacion=None, dimensiones=None):
        super().__init__(codigo, descripcion, materiales, datacion, dimensiones)