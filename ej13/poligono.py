from punto import Punto

class Poligono:
    def __init__(self):
        self.puntos = []

    def agregar_punto(self, punto):
        if not isinstance(punto, Punto):
            raise TypeError("Se debe añadir un objeto Punto")
        if punto.poligono is not None and punto.poligono is not self:
            raise ValueError("El punto ya pertenece a otro polígono")
        if punto not in self.puntos:
            self.puntos.append(punto)
            punto.set_poligono(self)

    def quitar_punto(self, punto):
        if punto in self.puntos:
            self.puntos.remove(punto)
            punto.set_poligono(None)

    def cantidad_puntos(self):
        return len(self.puntos)

    def es_valido(self):
        return self.cantidad_puntos() >= 3

    def __str__(self):
        return f"Poligono({[ (p.x,p.y) for p in self.puntos ]})"

    def __repr__(self):
        return f"Poligono({len(self.puntos)} puntos)"
