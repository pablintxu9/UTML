from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado
from elipse import Elipse


def main():
    c1 = Circulo(color="Negro", diametro=1)
    r1 = Rectangulo(longitud=3, anchura=1, color="Naranja")
    c2 = Cuadrado(longitud=1.5, color="Azul")
    e1 = Elipse(color="Amarillo", eje_mayor=3, eje_menor=1)

    print(f"c1: {c1}")
    print(f"r1: {r1}")
    print(f"c2: {c2}")
    print(f"e1: {e1}")


if __name__ == "__main__":
    main()
