from .punto import Punto
from .poligono import Poligono

def main():
    p1 = Punto(0, 0)
    p2 = Punto(10, 0)
    p3 = Punto(0, 10)

    pol = Poligono()
    pol.agregar_punto(p1)
    pol.agregar_punto(p2)
    pol.agregar_punto(p3)

    print("Poligono puntos:", pol.get_puntos())

if __name__ == "__main__":
    main()
