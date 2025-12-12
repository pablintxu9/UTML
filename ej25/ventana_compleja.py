class VentanaCompleja(Ventana):
    def __init__(self, descripcion, anchura, altura, tecnica_cierre):
        super().__init__(descripcion, anchura, altura)
        self.tecnica_cierre = tecnica_cierre