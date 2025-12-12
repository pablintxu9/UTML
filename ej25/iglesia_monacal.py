class IglesiaMonacal(Iglesia):
    def __init__(self, nombre, orden, direccion=None):
        super().__init__(nombre, direccion)
        self.orden = orden
        self.nave = None
        self.ventanas = []
        self.crucero = None
        self.abside = None

    def asignar_nave(self, nave):
        self.nave = nave

    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)

    def asignar_crucero(self, crucero):
        self.crucero = crucero

    def asignar_abside(self, abside):
        self.abside = abside