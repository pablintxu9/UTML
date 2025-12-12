from edificio import Edificio
from uso_edificio import UsoEdificio
from hospital import Hospital
from escuela import Escuela
from vivienda import Vivienda

def main():
    edificio = Edificio("E001")

    uso1 = UsoEdificio(Hospital(), "2020-01-01", "2022-12-31")
    uso2 = UsoEdificio(Escuela(), "2023-01-01", None)

    edificio.agregar_uso(uso1)
    edificio.agregar_uso(uso2)

    print(f"Edificio: {edificio.codigo}")
    for uso in edificio.usos:
        fin = uso.fecha_fin if uso.fecha_fin else "actualidad"
        print(f"- {uso.uso.nombre} desde {uso.fecha_inicio} hasta {fin}")

if __name__ == "__main__":
    main()