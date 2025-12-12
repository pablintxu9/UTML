from punto import Punto
from linea import Linea
from area import Area

def main():
    p1 = Punto("P001", "Punto A", 1, 2, 3)
    p2 = Punto("P002", "Punto B", 4, 5, 6)
    p3 = Punto("P003", "Punto C", 7, 8, 9)

    linea = Linea("L001", "Línea 1", [p1, p2])
    area = Area("A001", "Área 1", [p1, p2, p3])

    print("Línea:")
    linea.mostrar()
    print()

    print("Área:")
    area.mostrar()

if __name__ == "__main__":
    main()