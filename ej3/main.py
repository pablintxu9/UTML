from cuadro import Cuadro
from lugar import Lugar


def main():
    gioconda = Cuadro("Gioconda", "1503 - 1510", "Óleo", "Pincelado simple", "Madera de álamo", "Leonardo da Vinci", "Regular")
    louvre = Lugar("Museo del Louvre", "París", "Francia")
    gioconda.set_localiza_en(louvre)

    replica = Cuadro("Gioconda de El Prado", "1503 - 1516", "Óleo", "Pincelado simple", "Madera de nogal", "Desconocido", "Bueno")
    prado = Lugar("Museo de El Prado", "Madrid", "España")
    replica.set_localiza_en(prado)

    print("=== Gioconda ===")
    print(f"Título: {gioconda.titulo}")
    print(f"Año: {gioconda.anno}")
    print(f"Técnica: {gioconda.tecnica}")
    print(f"Sub-técnica: {gioconda.subtecnica}")
    print(f"Soporte: {gioconda.soporte}")
    print(f"Autor: {gioconda.autor}")
    print(f"Estado de conservación: {gioconda.estado}")
    print(f"Se localiza en: {gioconda.lugar}\n")

    print(f"Título: {replica.titulo}")
    print(f"Año: {replica.anno}")
    print(f"Técnica: {replica.tecnica}")
    print(f"Sub-técnica: {replica.subtecnica}")
    print(f"Soporte: {replica.soporte}")
    print(f"Autor: {replica.autor}")
    print(f"Estado de conservación: {replica.estado}")
    print(f"Se localiza en: {replica.lugar}")


if __name__ == "__main__":
    main()
