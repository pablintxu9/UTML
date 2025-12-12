from .punto import Punto
from .poligono import Poligono

def main():
    # Crear puntos compartidos para representar dos triángulos que comparten un lado
    p1 = Punto(-10, 10)
    p2 = Punto(-10, -10)
    p3 = Punto(10, -10)
    p4 = Punto(10, 10)

    # Primer triángulo t1: p1, p2, p3
    t1 = Poligono()
    t1.agregar_punto(p1)
    t1.agregar_punto(p2)
    t1.agregar_punto(p3)

    # Segundo triángulo t2: p1 (compartido), p3 (compartido), p4
    t2 = Poligono()
    t2.agregar_punto(p1)
    t2.agregar_punto(p3)
    t2.agregar_punto(p4)

    print("T1 puntos:", t1.get_puntos())
    print("T2 puntos:", t2.get_puntos())

if __name__ == "__main__":
    main()
from punto import Punto
from poligono import Poligono

def main():
    p1 = Punto(0, 0)
    p2 = Punto(1, 0)
    p3 = Punto(0.5, 1)
    p4 = Punto(1.5, 1)

    t1 = Poligono()
    t1.agregar_punto(p1)
    t1.agregar_punto(p2)
    t1.agregar_punto(p3)

    t2 = Poligono()
    t2.agregar_punto(p2)
    t2.agregar_punto(p3)
    t2.agregar_punto(p4)

    print(t1)
    print(t2)

if __name__ == "__main__":
    main()
