class IglesiaRural(Iglesia):
    def __init__(self, nombre, direccion=None):
        super().__init__(nombre, direccion)
        self.nave = None
        self.ventanas = []
        self.abside = None

    def asignar_nave(self, nave):
        self.nave = nave

    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)

    def asignar_abside(self, abside):
        self.abside = abside