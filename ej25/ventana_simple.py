class VentanaSimple(Ventana):
    def __init__(self, descripcion, anchura, altura, tiene_arco_doble, decorada, tecnica_cierre):
        super().__init__(descripcion, anchura, altura)
        self.tiene_arco_doble = tiene_arco_doble
        self.decorada = decorada
        self.tecnica_cierre = tecnica_cierre