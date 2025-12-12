from entidad_arqueologica import EntidadArqueologica

class SitioArqueologico(EntidadArqueologica):
    def __init__(self, cronologia, tipo):
        super().__init__(cronologia)
        self.tipo = tipo