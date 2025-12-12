from tipo_impresion import TipoImpresion
from tecnica_encuadernacion import TecnicaEncuadernacion

class Libro:
    def __init__(self, numero_hojas, forma_impresion, tecnica_encuadernacion):
        if forma_impresion not in TipoImpresion.TODOS:
            raise ValueError("Forma de impresión no válida.")
        if tecnica_encuadernacion not in TecnicaEncuadernacion.TODAS:
            raise ValueError("Técnica de encuadernación no válida.")
        self.numero_hojas = numero_hojas
        self.forma_impresion = forma_impresion
        self.tecnica_encuadernacion = tecnica_encuadernacion

    def mostrar(self):
        print(f"Número de hojas: {self.numero_hojas}")
        print(f"Forma de impresión: {self.forma_impresion}")
        print(f"Técnica de encuadernación: {self.tecnica_encuadernacion}")