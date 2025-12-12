from objeto import Objeto
from coleccion import Coleccion
from coleccion_temporal import ColeccionTemporal
from ubicacion import Ubicacion
from sala import Sala
from almacen import Almacen
from planta import Planta
from edificio import Edificio
from restauracion import Restauracion

def main():
    ubicacion1 = Ubicacion("U001")
    objeto1 = Objeto("O001", "Vasija", "Anónimo", "1200 a.C.", "Egipto", "Restaurado", ["Cerámica"], "Vasija decorada")
    objeto1.asignar_ubicacion(ubicacion1)

    coleccion = Coleccion("Antigüedades", "Objetos antiguos de diversas culturas")
    coleccion.agregar_objeto(objeto1)

    restauracion = Restauracion("2020-05-10", "Limpieza superficial", ["Cepillado", "Consolidación"])
    restauracion.agregar_objeto(objeto1)

    print("Objeto restaurado:")
    objeto1.mostrar()

if __name__ == "__main__":
    main()