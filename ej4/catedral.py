class Catedral:
    def __init__(self, nombre, culto, anno_inicio, fecha_primera, fecha_segunda, fecha_bic, material, estilos):
        self.nombre = nombre
        self.culto = culto
        self.anno_inicio = anno_inicio
        self.fecha_primera = fecha_primera
        self.fecha_segunda = fecha_segunda
        self.fecha_bic = fecha_bic
        self.material = material
        self.estilos = estilos
        self.lugar = None
        self.etapas_construccion = []
    
    def set_encuentra_en(self, lugar):
        self.lugar = lugar
    
    def agregar_etapa(self, etapa):
        if etapa not in self.etapas_construccion:
            self.etapas_construccion.append(etapa)
    
    def __str__(self):
        return self.nombre
    
    def __repr__(self):
        return f"Catedral('{self.nombre}')"
