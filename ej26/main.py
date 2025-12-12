from lugar import Lugar
from sitio_arqueologico import SitioArqueologico
from conjunto_arqueologico import ConjuntoArqueologico
from tipo_sitio import TipoSitio
from dimension import Dimension

def main():
    lugar1 = Lugar("Valle Sagrado", "Cusco", "Perú")
    sitio = SitioArqueologico("1200 a.C.", TipoSitio.ASENTAMIENTO)
    sitio.asignar_lugar(lugar1)
    sitio.agregar_dimension(Dimension("Altura", 15, "metros"))
    sitio.agregar_dimension(Dimension("Área", 2000, "m²"))

    conjunto = ConjuntoArqueologico("500 d.C.")
    conjunto.asignar_lugar(lugar1)

    print(f"Sitio Arqueológico en {sitio.lugar.nombre}, {sitio.lugar.provincia}, {sitio.lugar.pais}")
    print(f"- Tipo: {sitio.tipo}")
    print(f"- Cronología: {sitio.cronologia}")
    print("- Dimensiones:")
    for d in sitio.dimensiones:
        print(f"  - {d.nombre}: {d.medida} {d.unidad}")

    print()
    print(f"Conjunto Arqueológico en {conjunto.lugar.nombre}")
    print(f"- Cronología: {conjunto.cronologia}")

if __name__ == "__main__":
    main()