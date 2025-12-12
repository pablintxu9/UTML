from ciudad import Ciudad
from calle import Calle
from plaza import Plaza
from edificio import Edificio
from elemento_estructural import ElementoEstructural
from tipo_elemento import TipoElemento

def main():
    ciudad = Ciudad("Madrid", "Madrid", "España")

    calle = Calle("Gran Vía", 1300, ciudad)
    plaza = Plaza("Plaza Mayor", 4200, ciudad)

    ciudad.agregar_espacio(calle)
    ciudad.agregar_espacio(plaza)

    edificio1 = Edificio("E001", calle)
    edificio2 = Edificio("E002", plaza)

    calle.agregar_edificio(edificio1)
    plaza.agregar_edificio(edificio2)

    elemento1 = ElementoEstructural(TipoElemento.PUERTA, edificio1)
    elemento2 = ElementoEstructural(TipoElemento.BALCON, edificio2)

    edificio1.agregar_elemento(elemento1)
    edificio2.agregar_elemento(elemento2)

    print(f"Ciudad: {ciudad.nombre}, Provincia: {ciudad.provincia}, País: {ciudad.pais}")
    for espacio in ciudad.espacios_abiertos:
        print(f"- Espacio: {espacio.nombre}")
        for edificio in espacio.edificios:
            print(f"  - Edificio: {edificio.numero}")
            for elem in edificio.elementos:
                print(f"    - Elemento: {elem.tipo}")

if __name__ == "__main__":
    main()