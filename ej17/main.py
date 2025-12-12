from .biblioteca import Biblioteca
from .planta import Planta
from .tematica import Tematica
from .libro import Libro
from .ejemplar import Ejemplar
from .lector import Lector
from .empleado import Empleado
from .prestamo import Prestamo

def main():
    bib = Biblioteca("Biblioteca Central", "Calle Falsa 1", ["+34900123456"], 12, "1990")

    planta1 = Planta(1, 200)
    bib.add_planta(planta1)

    tem = Tematica("Historia")
    planta1.add_tematica(tem)

    libro = Libro("978-1234567890", "Historia Universal", "2005", ["ES"])
    libro.add_tematica(tem)
    bib.add_libro(libro)

    ej1 = Ejemplar("E-0001", "Editorial A", "2010")
    libro.add_ejemplar(ej1)

    lector = Lector("Ana López", "L-123", "C/ Verde 5")
    emp = Empleado("Jose", "EMP-01")

    prest = Prestamo("2025-12-01", "2025-12-15")
    prest.set_lector(lector)
    prest.set_empleado(emp)
    prest.add_ejemplar(ej1)

    print(bib)
    print("Plantas:", bib.plantas)
    print("Tematicas en planta1:", planta1.tematicas)
    print("Libros en biblioteca:", bib.libros)
    print("Ejemplares del libro:", libro.ejemplares)
    print("Prestamo:", prest)
    print("Lector prestamos:", lector.prestamos)

if __name__ == "__main__":
    main()
