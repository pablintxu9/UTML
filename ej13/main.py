from punto import Punto
from poligono import Poligono


def main():
    p1 = Punto(-10, 10)
    p2 = Punto(10, 10)
    p3 = Punto(10, -10)
    p4 = Punto(-10, -10)

    pol = Poligono()
    pol.agregar_punto(p1)
    pol.agregar_punto(p2)
    pol.agregar_punto(p3)
    pol.agregar_punto(p4)

    print("=== Polígono ===")
    print(pol)
    print(f"Cantidad de puntos: {pol.cantidad_puntos()}")
    print(f"Válido (>=3 puntos): {pol.es_valido()}")

    print("\nPuntos y su polígono:")
    for p in pol.puntos:
        print(f"  {p} -> pertenece a polígono: {p.poligono is pol}")


if __name__ == "__main__":
    main()
