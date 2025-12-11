from circulo import Circulo
from rectangulo import Rectangulo
from cuadrado import Cuadrado
from elipse import Elipse


def main():
    circulo = Circulo(color="Gris", diametro=1)
    rectangulo = Rectangulo(longitud=3, anchura=1, color="Naranja")
    cuadrado = Cuadrado(longitud=1, color="Azul")
    elipse = Elipse(color="Amarillo", eje_mayor=3, eje_menor=1)
    
    print(f"circulo: {circulo}")
    print(f"rectangulo: {rectangulo}")
    print(f"cuadrado: {cuadrado}")
    print(f"elipse: {elipse}")


if __name__ == "__main__":
    main()
