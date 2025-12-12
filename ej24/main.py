from libro import Libro
from muestra import Muestra
from tipo_impresion import TipoImpresion
from tecnica_encuadernacion import TecnicaEncuadernacion

def main():
    libro = Libro(250, TipoImpresion.IMPRESO, TecnicaEncuadernacion.ENCUADERNADO)
    muestra = Muestra(0.1, "Aleatoria estratificada")

    print("Libro:")
    libro.mostrar()
    print()

    print("Muestra:")
    muestra.mostrar()

if __name__ == "__main__":
    main()