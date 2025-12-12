from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circulo import Circulo
from elipse import Elipse

def main():
    cuad = Cuadrado("Rojo", 5)
    rect = Rectangulo("Azul", 10, 4)
    circ = Circulo("Verde", 7)
    elip = Elipse("Amarillo", 8, 5)

    print("Cuadrado:")
    cuad.mostrar()
    print()

    print("Rectangulo:")
    rect.mostrar()
    print()

    print("Circulo:")
    circ.mostrar()
    print()

    print("Elipse:")
    elip.mostrar()
    print()

if __name__ == "__main__":
    main()